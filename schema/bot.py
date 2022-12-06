# Init Schemas base action
newSchema = SchemaDate("tBot", "bot")
CS = dict()
CS['sort'] = 0
CS['actions'] = list()
CS['actions'].append({'do':'act', 'act': 'bot_new_user', 'event': 'new_user'})
CS['actions'].append({'do':'act', 'act': 'bot_append_chat', 'event': 'append_chat'})
CS['actions'].append({'do':'act', 'act': 'bot_send_file', 'event': 'send_file'})
CS['actions'].append({'do':'act', 'act': 'bot_write_command', 'event': 'write_command'})
CS['actions'].append({'do':'act', 'act': 'bot_write_text', 'event': 'write_text'})
CS['actions'].append({'do':'act', 'act': 'bot_check_chat_user', 'event': 'check_chat_user'})

newSchema.ConfigStruct(CS)
#Add to load core
param['schema'].append(newSchema)
