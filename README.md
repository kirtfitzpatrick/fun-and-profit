# Fun & Profit

AWS Cloud Development Kit app. It's just an excuse for me to 
play around with CDK and python.

## Current Experiments

### Autocomplete

[Typing is for suckers.](https://gist.github.com/kirtfitzpatrick/e7a7828e99bae609955f08b35fc2c8b1)
```
function _cdk_completer {
  STACK_CMDS="list synthesize bootstrap deploy destroy diff metadata init context docs doctor"

  if [ "$3" == "cdk" ]; then
    COMPREPLY=($(compgen -W "$STACK_CMDS" $2))
  elif [[ -d "cdk.out" ]] && ! [[ "$2" == "-"* ]]; then
    TEMPLATES=$(ls -1 cdk.out/*.template.json | awk '{split($0,t,/\/|\./); print t[3]}')
    COMPREPLY=($(compgen -W "$TEMPLATES" $2))
  else
    COMPREPLY=()
  fi
}
complete -F _cdk_completer cdk
```

### Trying To Scope Stacks With Constructs

```bash
$ cdk metadata FnpDevHelloDocker434A33B3 
/Fnp/Dev/HelloDocker:
  - type: aws:cdk:stack-tags
    data:
      - key: Org
        value: Fnp
      - key: Env
        value: Dev
      - key: Name
        value: FnpDevHelloDocker
/Fnp/Dev/HelloDocker/TaskDef/TaskRole/Resource:
  - type: aws:cdk:logicalId
    data: TaskDefTaskRole1EDB4A67
/Fnp/Dev/HelloDocker/TaskDef/Resource:
  - type: aws:cdk:logicalId
    data: TaskDef54694570
/Fnp/Dev/HelloDocker/TaskDef/ExecutionRole/Resource:
  - type: aws:cdk:logicalId
    data: TaskDefExecutionRoleB4775C97
/Fnp/Dev/HelloDocker/TaskDef/ExecutionRole/DefaultPolicy/Resource:
  - type: aws:cdk:logicalId
    data: TaskDefExecutionRoleDefaultPolicy0DBB737A
/Fnp/Dev/HelloDocker/Service/Service:
  - type: aws:cdk:logicalId
    data: ServiceD69D759B
```

### Using direnv to Configure The Command Line Environment

```bash
cat dot_profile >> ~/.profile
. !$
cp dot_envrc .envrc
vim !$
reload-direnv
```

Add your config stuff to .envrc and away you go.