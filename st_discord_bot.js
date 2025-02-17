"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var discord_js_1 = require("discord.js");
var bot = new discord_js_1.Client({
    intents: [
        discord_js_1.GatewayIntentBits.Guilds,
        discord_js_1.GatewayIntentBits.GuildMembers,
        discord_js_1.GatewayIntentBits.GuildVoiceStates,
    ],
});
bot.once("ready", function () {
    var _a;
    console.log("".concat((_a = bot.user) === null || _a === void 0 ? void 0 : _a.tag, " is ready!"));
    console.log(bot.guilds.cache);
});
bot.on("voiceStateUpdate", function (before, after) { return __awaiter(void 0, void 0, void 0, function () {
    var guild, member, roleName, channelIds, role, role;
    var _a;
    return __generator(this, function (_b) {
        switch (_b.label) {
            case 0:
                guild = (_a = after.guild) !== null && _a !== void 0 ? _a : before.guild;
                if (!guild)
                    return [2 /*return*/];
                member = guild.members.cache.get(after.id) || guild.members.cache.get(before.id);
                // If member is undefined or a bot we exit the function.
                if (!member || member.user.bot)
                    return [2 /*return*/];
                roleName = "studying";
                channelIds = [1234, 5678];
                if (!(after.channel && channelIds.includes(Number(after.channel.id)))) return [3 /*break*/, 2];
                role = guild.roles.cache.find(function (r) { return r.name === roleName; });
                if (!role) return [3 /*break*/, 2];
                return [4 /*yield*/, member.roles.add(role, "User joined studying voice channel")];
            case 1:
                _b.sent();
                _b.label = 2;
            case 2:
                if (!(before.channel && channelIds.includes(Number(before.channel.id)))) return [3 /*break*/, 4];
                role = guild.roles.cache.find(function (r) { return r.name === roleName; });
                if (!role) return [3 /*break*/, 4];
                return [4 /*yield*/, member.roles.remove(role, "User left studying voice channel")];
            case 3:
                _b.sent();
                _b.label = 4;
            case 4: return [2 /*return*/];
        }
    });
}); });
bot.login("someKey");
