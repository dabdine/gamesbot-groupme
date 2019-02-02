# gamesbot-groupme
A simple bot that listens for a trigger in a chat channel (specified by a regex), and responds using a meme image link.

# deploying
1. Create an AWS account, including access keys.
2. Install serverless framework.
3. Run `sls deploy` from the command line on this repo. It will print out a URL under "endpoints". Copy that URL.
4. Go to https://dev.groupme.com/bots. Create a new bot. Fill in the callback URL with the URL you received from step 3. Copy the bot ID.
5. Re-run the deployment, specifying the bot ID you copied from step 4, and the trigger regex + image link you want to use: `GROUPME_BOT_TRIGGER_REGEX="<FILL THIS IN>" GROUPME_BOT_ID="<FILL THIS IN>" GROUPME_IMAGE_LINK="<FILL THIS IN>" sls deploy`
6. Type your trigger word matching the regex you specified into your group chat, and enjoy.

# debugging
Use `sls logs -f message` to see output from the lambda that runs on AWS.

# undeploying/removing
1. Run `sls remove`
2. Delete the bot you added from https://dev.groupme.com/bots.

# cost
The cost to run this should fall completely within the AWS free tier. The lambda uses 128MB of RAM, and generally takes 200ms to execute completely.
The AWS Lambda and AWS API Gateway that are created when this project is deployed have a free tier of 1m requests (ignoring other factors since
they're negligible, such as compute time).
