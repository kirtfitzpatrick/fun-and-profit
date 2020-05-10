# Fun & Profit

AWS Cloud Development Kit app. It's just an excuse for me to 
play around with CDK and python.

## Current Experiments

### Autocomplete

Typing is for suckers. 👉 [gist](https://gist.github.com/kirtfitzpatrick/e7a7828e99bae609955f08b35fc2c8b1)

```bash
$ cdk 
bootstrap   context     deploy      destroy     diff        docs        doctor      init        list        metadata    synthesize  
$ cdk metadata Fnp
FnpDevHelloDocker434A33B3  FnpDevNetwork67514EC7      FnpDevPublicEcs45E75100    FnpDevTweetIngestC12A26E5  FnpRegistryB3019273        
$ cdk metadata FnpDev
FnpDevHelloDocker434A33B3  FnpDevNetwork67514EC7      FnpDevPublicEcs45E75100    FnpDevTweetIngestC12A26E5  
$ cdk metadata FnpDevHelloDocker434A33B3
```

### Trying To Scope Stacks With Constructs

That hash appended to everything except the base node of the tree is KILLING ME!

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

### Using direnv To Configure Local Development

Add your config stuff to .envrc and away you go.
With any luck this codebase will be a 12 factor app. ;-)

```bash
cat dot_profile >> ~/.profile
. !$
cp dot_envrc .envrc
vim !$
reload-direnv
```
