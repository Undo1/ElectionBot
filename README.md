# ElectionBot

A bot to post results from Stack Exchange moderator elections to chatrooms.

## Usage

Before election ends, download everything:

```
git clone https://github.com/Undo1/ElectionBot.git
cd ElectionBot
git submodule init
git submodule update
```

When election is about to end, run:

```
python StackElectChat.py <site> <election number> <chatroom ID>
```

For example, to get results from Stack Overflow's 1st election posted to [this room](http://chat.stackexchange.com/rooms/17251/smoke-detector-school), you would run this:

```
python StackElectChat.py stackoverflow.com 1 17251
```

It'll ask you for your username and password. It's advised that you create a seperate chatbot account with a Stack Exchange OpenID. ChatExchange, and therefore this bot, only accepts SE OpenIDs. Your username is your email address.

After the chat connection is verified, it'll wait for your command - useful for getting everything ready before an election ends. Right after the election phase is over, press [Enter] and wait. It'll get the ballot file and run Meek STV on it. It will then show you the results, asking if it's okay to post. Enter 'y' and it'll go do it.
