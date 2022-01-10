# private_wall

## Objectives

- Practice connecting a Flask application to a MySQL database
- Include login and registration
- Self Join relationships
- Continue to think about web security and how others could potentially hack your site

For this assignment, a user's "wall" is a list of their private messages. Once a user has logged in, they can view their wall and, on this same page, the logged in user can also send messages to other users. The yellow sticky notes indicate basic functionality. Review the green sticky notes for Ninja Bonuses and purple sticky notes for Sensei Bonuses.

<img width="634" alt="Screen Shot 2022-01-09 at 8 10 33 PM" src="https://user-images.githubusercontent.com/92617960/148714176-8b8315f7-c353-4a14-b9d8-2ff5896b4363.png">

## Additional Sensei Bonus

For the delete functionality, do not allow someone to remove a message that doesn't belong to them. If someone tries to remove a message that doesn't belong to them, have your app display the following:

<img width="466" alt="Screen Shot 2022-01-09 at 8 11 05 PM" src="https://user-images.githubusercontent.com/92617960/148714205-3e355055-58d3-493a-8f81-7d96270f392b.png">

You don't really need to build the feature to report the IP address, but do log the user out if they try to remove a message that doesn't belong to them for the second time in a row. We'll leave it up to you to find out how to find the IP address of the user (a simple google search will show you how to do this in Flask).
