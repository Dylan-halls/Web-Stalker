# Web-Stalker
Web Stalker is a tool that when used along side packet redirection can be very useful
in helping an attacker gather information about there victims habits and data presence on the internet. 
It does this by capturing all of the victims HTTP packets, thus allowing the attacked to view there complete 
HTTP Requests and the Servers Responce (This includes storing there post data)

Web Stalker uses gtk binding in python to offer the attacker to most comfy enviroment
in which the can work.

To use it the command is:

    python webstalker.py
    
And that will begin the packet listener

Then once you our ready you can ^C out of it and a GUI will open up with all of the packets 
and data in a extremly readable format.

And you can analyse the data on the fly by using the data shown in the terminal, and every
HTTP Request haveing a link the the site and page that the victim is on.

There is an additional option of being able to view a targets website with a specialy designed 'Web Stalker Browser'
that will allow you to navigate the sites with ease and efficiancy

There is also the option to record and save notes on a in window note pad. This opens up a whole load of doors with it being
possable to save the text in any format meaning you could write a web report for your finding in 
HTML or PHP or write a GUI in C to disply it, or evan create a whole markdown page!
