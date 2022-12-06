# Init Schemas base action
newSchema = SchemaDate("start_up", "init")
CS = dict()
CS['sort'] = 15
CS['actions'] = list()
CS['actions'].append({'do' : 'act', 'act' : 'StartUpApp'})
#CS['actions'].append({'obj': 'varObj', 'do': 'save', 'target': 'config'})
#CS['actions'].append({'do': 'finish'})

newSchema.ConfigStruct(CS)
#Add to load core
param['schema'].append(newSchema)
