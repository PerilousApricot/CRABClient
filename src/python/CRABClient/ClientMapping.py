#!/usr/bin/env python
"""
_ClientMapping_

This allows to have an agnostic client.
For each client command it is possible to define the path of the REST request, the map between
the client configuration and the final request to send to the server. It includes type of the
parameter so that the client can do a basic sanity check on the input data type.
For each server parameter, there can be more than one parameter in the CRAB configuration file.
If that is the case, then the meaning is that any of the parameters in the CRAB configuration
file is used to set the same server parameter.
"""

## In this dictionary, the definitions of 'type', 'required' and 'default'
## refer to the parameters in the CRAB configuration file.
parametersMapping = {
    'on-server': {'workflow'       : {'default': None,       'config': ['General.requestName'],             'type': 'StringType',  'required': False},
                  'activity'       : {'default': None,       'config': ['General.activity'],                'type': 'StringType',  'required': False},
                  'saveoutput'     : {'default': True,       'config': ['General.transferOutputs'],         'type': 'BooleanType', 'required': False},
                  'savelogsflag'   : {'default': False,      'config': ['General.transferLogs'],            'type': 'BooleanType', 'required': False},
                  'faillimit'      : {'default': None,       'config': ['General.failureLimit'],            'type': 'IntType',     'required': False},
                  'inputdata'      : {'default': None,       'config': ['Data.inputDataset',
                                                                        'Data.primaryDataset'],             'type': 'StringType',  'required': False},
                  'userfiles'      : {'default': None,       'config': ['Data.userInputFiles'],             'type': 'ListType',    'required': False},
                  'dbsurl'         : {'default': 'global',   'config': ['Data.inputDBS'],                   'type': 'StringType',  'required': False},
                  'useparent'      : {'default': None,       'config': ['Data.useParent'],                  'type': 'BooleanType', 'required': False},
                  'ignorelocality' : {'default': False,      'config': ['Data.ignoreLocality'],             'type': 'BooleanType', 'required': False},
                  'splitalgo'      : {'default': None,       'config': ['Data.splitting'],                  'type': 'StringType',  'required': True },
                  'algoargs'       : {'default': None,       'config': ['Data.unitsPerJob'],                'type': 'IntType',     'required': True },
                  'totalunits'     : {'default': 0,          'config': ['Data.totalUnits'],                 'type': 'IntType',     'required': False},
                  'lfn'            : {'default': None,       'config': ['Data.outLFNDirBase'],              'type': 'StringType',  'required': False},
                  'publication'    : {'default': True,       'config': ['Data.publication'],                'type': 'BooleanType', 'required': False},
                  'publishdbsurl'  : {'default': 'phys03',   'config': ['Data.publishDBS'],                 'type': 'StringType',  'required': False},
                  'publishname'    : {'default': '',         'config': ['Data.publishDataName'],            'type': 'StringType',  'required': False},
                  'jobtype'        : {'default': 'Analysis', 'config': ['JobType.pluginName',
                                                                        'JobType.externalPluginFile'],      'type': 'StringType',  'required': False},
                  'generator'      : {'default': 'pythia',   'config': ['JobType.generator'],               'type': 'StringType',  'required': False},
                  'eventsperlumi'  : {'default': None,       'config': ['JobType.eventsPerLumi'],           'type': 'IntType',     'required': False},
                  'adduserfiles'   : {'default': [],         'config': ['JobType.inputFiles'],              'type': 'ListType',    'required': False},
                  'addoutputfiles' : {'default': [],         'config': ['JobType.outputFiles'],             'type': 'ListType',    'required': False},
                  'maxjobruntime'  : {'default': None,       'config': ['JobType.maxJobRuntimeMin'],        'type': 'IntType',     'required': False},
                  'numcores'       : {'default': None,       'config': ['JobType.numCores'],                'type': 'IntType',     'required': False},
                  'maxmemory'      : {'default': None,       'config': ['JobType.maxMemoryMB'],             'type': 'IntType',     'required': False},
                  'priority'       : {'default': None,       'config': ['JobType.priority'],                'type': 'IntType',     'required': False},
                  'nonprodsw'      : {'default': False,      'config': ['JobType.allowUndistributedCMSSW'], 'type': 'BooleanType', 'required': False},
                  'scriptexe'      : {'default': None,       'config': ['JobType.scriptExe'],               'type': 'StringType',  'required': False},
                  'scriptargs'     : {'default': None,       'config': ['JobType.scriptArgs'],              'type': 'ListType',    'required': False},
                  'asyncdest'      : {'default': None,       'config': ['Site.storageSite'],                'type': 'StringType',  'required': False},
                  'sitewhitelist'  : {'default': None,       'config': ['Site.whitelist'],                  'type': 'ListType',    'required': False},
                  'siteblacklist'  : {'default': None,       'config': ['Site.blacklist'],                  'type': 'ListType',    'required': False},
                  'vorole'         : {'default': None,       'config': ['User.voRole'],                     'type': 'StringType',  'required': False},
                  'vogroup'        : {'default': None,       'config': ['User.voGroup'],                    'type': 'StringType',  'required': False},
                  'oneEventMode'   : {'default': False,      'config': ['Debug.oneEventMode'],              'type': 'BooleanType', 'required': False},
                  'asourl'         : {'default': None,       'config': ['Debug.ASOURL'],                    'type': 'StringType',  'required': False},
                  'scheddname'     : {'default': None,       'config': ['Debug.scheddName'],                'type': 'StringType',  'required': False},
                  'extrajdl'       : {'default': None,       'config': ['Debug.extraJDL'],                  'type': 'ListType',    'required': False},
                  'collector'      : {'default': None,       'config': ['Debug.collector'],                 'type': 'StringType',  'required': False},
                 },
    'other-config-params': [         {'default': None,       'config': ['General.workArea'],                'type': 'StringType',  'required': False},
                                     {'default': 'prod',     'config': ['General.instance'],                'type': 'StringType',  'required': True },
                                     {'default': None,       'config': ['Data.lumiMask'],                   'type': 'StringType',  'required': False},
                                     {'default': None,       'config': ['Data.runRange'],                   'type': 'StringType',  'required': False},
                                     {'default': None,       'config': ['JobType.psetName'],                'type': 'StringType',  'required': False},
                                     {'default': False,      'config': ['JobType.sendPythonFolder'],        'type': 'BooleanType', 'required': False},
                                     {'default': None,       'config': ['JobType.pyCfgParams'],             'type': 'ListType',    'required': False},
                                     {'default': False,      'config': ['JobType.disableAutomaticOutputCollection'],'type': 'BooleanType', 'required': False},
                           ]
}

renamedParams = {
    'General.transferOutput'          : {'newParam' : 'General.transferOutputs',         'version' : None},
    'General.saveLogs'                : {'newParam' : 'General.transferLogs',            'version' : None},
    'Data.outlfn'                     : {'newParam' : 'Data.outLFNDirBase',              'version' : 'v3.3.16'},
    'Data.outLFN'                     : {'newParam' : 'Data.outLFNDirBase',              'version' : 'v3.3.16'},
    'Data.dbsUrl'                     : {'newParam' : 'Data.inputDBS',                   'version' : None},
    'Data.publishDbsUrl'              : {'newParam' : 'Data.publishDBS',                 'version' : None},
    'Data.userInputFile'              : {'newParam' : 'Data.userInputFiles',             'version' : None},
    'JobType.numcores'                : {'newParam' : 'JobType.numCores',                'version' : None},
    'JobType.maxmemory'               : {'newParam' : 'JobType.maxMemoryMB',             'version' : None},
    'JobType.maxjobruntime'           : {'newParam' : 'JobType.maxJobRuntimeMin',        'version' : None},
    'JobType.allowNonProductionCMSSW' : {'newParam' : 'JobType.allowUndistributedCMSSW', 'version' : 'v3.3.16'},
}


"""
---------------------------------------------------------------------------------------------------------------
Parameter Name          |  Parameter Meaning
---------------------------------------------------------------------------------------------------------------
requiresTaskOption      -  Whether the command requires the -d/--dir option or not (in the end, if the command
                           requiresa CRAB project directory as input). For the uploadlog command, we set this
                           to True even if the command accepts a path to a log file via the --logpath option
                           (in which case a CRAB project directory is not needed) and if the --logpath option
                           was given we set requiresTaskOption to False on the fly.
useCache                -  Whether to use the CRAB cache file (~/.crab3).
                           Currently only used to get the CRAB project directory in case the command requires
                           it but no directory was given in the -d/--dir option.
requiresREST            -  Whether the command has to contact the CRAB Server REST Interface.
acceptsArguments        -  Whether the command accepts arguments. (To not confuse with options.)
                           For commands requiring the task option, which can be actually given as an argument,
                           do not count it here as an argument. Same thing for the 'submit' command which can
                           take the CRAB configuration file name from the arguments.
initializeProxy         -  Whether the command needs to create a proxy if there is not a (valid) one already.
requiresProxyVOOptions  -  Whether the command requires the --voGroup and --voRole options or not.
doProxyGroupRoleCheck   -  Whether to check if the VO group and VO role in the proxy are the same as what has
                           been specified either in the CRAB configuration file or in the command options
                           --voGroup/--voRole (or with what is written in the request cache).
---------------------------------------------------------------------------------------------------------------
WARNING: Don't set at the same time acceptsArguments = True and requiresTaskOption = True. This is because
         we don't have a way to distinghish the CRAB project directory  name from the other arguments,
         so there is a protection when requiresTaskOption = True to not accept more that 1 argument.
---------------------------------------------------------------------------------------------------------------
"""
commandsConfiguration = {
    'checkusername' : {'acceptsArguments': False, 'requiresREST': False, 'initializeProxy': True,  'requiresTaskOption': False, 'useCache': False, 'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'checkwrite'    : {'acceptsArguments': False, 'requiresREST': False, 'initializeProxy': True,  'requiresTaskOption': False, 'useCache': False, 'requiresProxyVOOptions': True,  'doProxyGroupRoleCheck': True },
    'getlog'        : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': True,  'doProxyGroupRoleCheck': True },
    'getoutput'     : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': True,  'doProxyGroupRoleCheck': True },
    'kill'          : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': False, 'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'proceed'       : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'purge'         : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': False, 'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'remake'        : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': False, 'useCache': False, 'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'remote_copy'   : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': False, 'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'report'        : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'request_type'  : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'resubmit'      : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'status'        : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'submit'        : {'acceptsArguments': True,  'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': False, 'useCache': False, 'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': True },
    'tasks'         : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': False, 'useCache': False, 'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False},
    'uploadlog'     : {'acceptsArguments': False, 'requiresREST': True,  'initializeProxy': True,  'requiresTaskOption': True,  'useCache': True,  'requiresProxyVOOptions': False, 'doProxyGroupRoleCheck': False}
}


def revertParamsMapping():
    import copy
    revertedMapping = {}
    for serverParamName, paramInfo in parametersMapping['on-server'].iteritems():
        info = copy.deepcopy(paramInfo)
        info.pop('config')
        for clientParamName in paramInfo['config']:
            revertedMapping[clientParamName] = {'server': serverParamName}
            revertedMapping[clientParamName].update(info)
    for paramInfo in parametersMapping['other-config-params']:
        info = copy.deepcopy(paramInfo)
        info.pop('config')
        for clientParamName in paramInfo['config']:
            revertedMapping[clientParamName] = {'server': None}
            revertedMapping[clientParamName].update(info)
    return revertedMapping

## This mapping looks like this:
## {'General.requestName'     : {'server': 'workflow',   'default': None,  'type': 'StringType',  'required': False},
##  'General.activity'        : {'server': 'activity',   'default': None,  'type': 'StringType',  'required': False},
##  'General.transferOutputs' : {'server': 'saveoutput', 'default': True,  'type': 'BooleanType', 'required': False},
##  etc, for all CRAB configuration parameters
## }
configParametersInfo = revertParamsMapping()


def getParamServerName(paramName):
    return configParametersInfo.get(paramName, {}).get('server')


def getParamDefaultValue(paramName):
    return configParametersInfo.get(paramName, {}).get('default')

