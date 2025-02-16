import { Client, GatewayIntentBits, GuildMember, VoiceState, Role } from 'discord.js';
import { get } from 'lodash';

const bot = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildVoiceStates,
  ],
});

bot.once('ready', () => {
  console.log(`${bot.user?.tag} is ready!`);
  console.log(bot.guilds.cache);
});

bot.on('voiceStateUpdate', async (member: GuildMember, before: VoiceState, after: VoiceState) => {
  if (member.user.bot) return;

  const guild = member.guild;

  const roleName = "studying";
  const channelIds = [1234, 5678];

  if (after.channel && channelIds.includes(after.channel.id)) {
    const role = guild.roles.cache.find((r) => r.name === roleName);
    if (role) {
      await member.roles.add(role, "User joined studying voice channel");
    }
  }

  if (before.channel && channelIds.includes(before.channel.id)) {
    const role = guild.roles.cache.find((r) => r.name === roleName);
    if (role) {
      await member.roles.remove(role, "User left studying voice channel");
    }
  }
});

bot.login('someKey');
