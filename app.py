"""
Sample application using object detection and centroid tracking to
determine the number of non-unique people who pass in view, as well
display general metrics on total number of people, average time seen,
and longest time detected.
"""

import time
import edgeiq
import metrics_manager
import file_manager

CENTROID_TRACKER = "centroid_tracker"
METRICS_MANAGER = "metrics_manager"
DETECT_CONFIDENCE_THRESHOLD = .8
TRACKER_DEREGISTER_FRAMES = 20
TRACKER_MAX_DISTANCE = 50


def main():
    # Spin up the object detector
    obj_detect = edgeiq.ObjectDetection("alwaysai/mobilenet_ssd")
    obj_detect.load(engine=edgeiq.Engine.DNN)

    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Model:\n{}\n".format(obj_detect.model_id))

    # Prepare to track frames per second calculations
    fps = edgeiq.FPS()

    # Load any prior instance of the tracker, otherwise spin up a new one
    centroid_tracker = file_manager.load(CENTROID_TRACKER, edgeiq.CentroidTracker(
        deregister_frames=TRACKER_DEREGISTER_FRAMES, max_distance=TRACKER_MAX_DISTANCE))
    # Load any prior instance of the metrics data, otherwise start a new one
    metrics = file_manager.load(
        METRICS_MANAGER, metrics_manager.MetricsManager())

    try:

        with edgeiq.WebcamVideoStream(cam=2) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            # Loop detection and centroid tracker
            while True:
                metrics.newLoop()
                frame = video_stream.read()
                results = obj_detect.detect_objects(
                    frame, confidence_level=DETECT_CONFIDENCE_THRESHOLD)

                # Ignore detections of anything other than people
                filter = edgeiq.filter_predictions_by_label(
                    results.predictions, ['person'])

                # Adding info for streamer display
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                    "Inference time: {:1.3f} s".format(results.duration))
                text.append("People currently detected:")

                objects = centroid_tracker.update(filter)

                # Store active predictions for just this loop
                predictions = []
                # Store the active object ids for just this loop

                if len(objects.items()) == 0:
                    # No people detected
                    text.append("-- NONE")

                for (object_id, prediction) in objects.items():
                    metrics.addTimeFor(object_id)
                    timeForId = metrics.timeForId(object_id)
                    # Correcting for fact that index 0 is first object in an array
                    idAdjusted = object_id + 1
                    # Display text with bounding box in video
                    new_label = "Person {i} | {t} sec".format(
                        i=idAdjusted, t=timeForId)
                    prediction.label = new_label
                    text.append(new_label)
                    predictions.append(prediction)

                # Add metrics to text going to streamer
                m = metrics.currentMetrics()
                text.append("")  # Spacing
                text.append("Total people seen: {}".format(m["count"]))
                text.append("Total time: {} sec".format(m["total"]))
                text.append("Average time: {0:.1f} sec".format(m["avg"]))
                text.append(
                    "Longest individual time: {} sec".format(m["max"]))

                # Update output streamer
                frame = edgeiq.markup_image(frame, predictions)
                streamer.send_data(frame, text)
                fps.update()

                if streamer.check_exit():
                    break

    finally:
        fps.stop()
        # TODO: Update to save every few seconds in case a crash occurs
        file_manager.save(metrics, METRICS_MANAGER)
        file_manager.save(centroid_tracker, CENTROID_TRACKER)
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))
        print("Program Ending")


if __name__ == "__main__":
    main()
