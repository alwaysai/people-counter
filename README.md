# People Counter App
This app expands on the alwaysAI face counter starter app to both count the number of non-unique people (same person will be counted multiple times if they exit and re-enter the frame) detecdted and to display basic time metrics on those appearances.

## Setup
This app requires access to alwaysAI's Beta program. To apply goto the [Sign up page](https://dashboard.alwaysai.co/docs/getting_started/introduction.html)

Once accepted to the program, follow the setup instructions located on the [Docs page](https://dashboard.alwaysai.co/docs/getting_started/introduction.html) - Note this link is accessible only to beta users.

## Persistence
The metric_manager saves a record of visits with each newLoop() call. To reset, delete the `visits.json` file.

## Usage
Once the alwaysAI toolset is installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & folder path
`aai app configure`

To install the app on the target device
`aai app install`

To start the app
`aai app start`
