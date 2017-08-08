# DSA Sign In Sheets

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PhillyDSA/dsa-sign-in-sheets)

## Purpose

This software was created to fill a need in our local chapter to have folks that attend meetings be able to sign in electronically. There are a few benefits to this:

- Organizers don't have to retype paper sign in sheets, which can result in errors and is a waste of their time and energy;
- It's pretty easy to steal a paper sign in sheet, whereas a laptop is more difficult; and
- We can enforce some basic security measures to protect our members.

To that end, we created a relatively simple web application that can be deployed to a free online host (Heroku) with no programming knowledge. We don't make any assumptions as to how you'll eventually store your member information; everything can be exported to a CSV file (basically a simpler Excel file) and they you can use it as you like.

## How to use this software

We've tried to make this as robust and easy-to-use as possible. That said, things go wrong, updates happen, and URLs change, so if there are any issues, open an issue (above - you'll need a Github account) or email [Jeremy](mailto:jeremy@iseverythingstilltheworst.com) and we'll get things sorted out.

_These instructions may seem long, but we've tried to be as detailed as possible for non-technical users, so don't be put off by the number of steps. It's not that bad! By the end, you'll have electronic sign in sheets for your local._

##### First things first:

1.	Sign up for a free account on [Heroku](https://heroku.com). They want an email address, etc. but they also want to know what programming language you'll be using. Select "Python" (it really doesn't matter) and you'll be good to go.
2.	Confirm your Heroku account. They'll send you an email.
3.	Come back here and click on the "Deploy to Heroku" button above. ("Deploy" here means start it running in Heroku-speak.)
4.	You'll be presented with a page to deploy your application. The only thing that you might/should want to change is the "App Name".
	- The name you choose will determine the website name where folks sign in. If you choose for example "phillydsa", the address for the site will be `phillydsa.herokuapp.com`.
	- If you don't make a choice there, a (usually) silly name will be assigned.
5. Don't make any other changes on the page unless you have a really good reason to.
6. At the bottom, there's a big button that says "Deploy". Click on that and you'll see a bunch of stuff happen, which just means that your site is being configured! It might take a while, so just hold tight.
7. Awesome! So when all's done on the backend, you should see a "View App" button appear. Click on that.

##### At this point, the app is running and we need to create a user to manage it.

1.	If you've gone through the steps above, you'll be presented with a page to either create an account or sign in. We'll assume this is your frist run.
2.	Click on the "Start Here" button.
3.	You'll be presented with a page to create an admin account. Choose your username and password. Click on "Create admin user" when you're ready to proceed.
4.	You'll then be presented with the log in page. Login using the account you just created.

##### Now we'll create an event.

1.	OK, so you've logged in and are ready to go. Click on the "Create Event" button. (If you have multiple events already created, that button disappears, but there's a link for "New Event" at the top of the page.)
2.	Choose a title for your event and a date for when your event will take place.
3.	Click on "Create Event" and you'll head over to the confirmation page.

<hr>

##### A brief interlude about security

**Please sign out of your Heroku account now. If your computer is stolen and you're still signed in, then that's a problem. There's no good way for us to mitigate against this, so it's up to you**.

<hr>

OK, back to it.

1.	If you're ready to sign people in, click on the "Sign out and go to event." This will drop you out of your admin account and allow folks to sign into your event.
2.	If you've already signed everyone into your event and you'd like to get the list of participants, click "Show Participants" at which point you'll be shown the first name of everyone that came and given an option to download the full CSV file (which has all the other fields).
3.	If you're all done with the event and **very sure about that fact**, you can "Delete Event." You'll be given a confirmation page before it's actually deleted, but this deletes all the data in the system about that one event and there's no way to get it back. Make sure to export to the CSV file first.

If you want to delete absolutely everything, sign into Heroku, click on the app you created, go to the "Settings" tab and all the way at the bottom, there's a red button that says "Delete app". You can always re-deploy the app if you need it again, but all your data will be gone.

##### And that's all!

If you have any questions that weren't answered, please file an issue (just click on the "Issues" tab above). If you use and like this software, let us know! Any suggestions? Let! Us! Know!

Anyway, seriously, hope you like it and the instructions were clear.
