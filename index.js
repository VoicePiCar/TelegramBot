'use strict';

var TelegramBot = require('node-telegram-bot-api');

var token = '212766013:AAH4tIpm6hHZREsxYNuYdCdNbw6CDlwV094';
// Setup polling way
var bot = new TelegramBot(token, {polling: true});

// Matches /echo [whatever]
bot.onText(/\/echo (.+)/, function (msg, match) {
    var fromId = msg.from.id;
    var resp = match[1];
    bot.sendMessage(fromId, resp);
});

// Catch voice messages
bot.on('voice', function (msg) {
    var chatId = msg.chat.id;
    console.log(msg);
    bot.downloadFile(msg.voice.file_id, "./sound").then(function (path) {
        console.log(path);
    });
    bot.sendMessage(chatId, "Voice!");
});
