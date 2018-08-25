# RT cosmo application control aka RLX3 starter

## Overview

The purpose of this document is to create a proposal for the RT cosmo application control, e.g. start, stop, status.

Find below the current state and the proposals for the RT cosmo application control.

## Current state

The RT cosmo application is controlled by the ```rlx3-starter``` as depicted in the figure below.

![RT cosmo current - components](0_rtcosmo_app_mng_component_current.png)

Systemd runs the RLX3 starter. Afterwards the RLX3 starter fires the script ```start.sh``` which basically starts the RT cosmo application.

This solution ends up with the following processes on the system.

![RT cosmo current - process tree](0_rtcosmo_app_mng_tree_current.png)

***note***: *The RLX3 starter is not in the processes list since the RLX3 starter service unit has Type=```forking``` (hence the RLX3 starter exits as the RT cosmo ```start.sh``` is daemonized).*

### Drawbacks
- daemonize package is required
- several process are running on top of the RT cosmo application
- service unit file is separated from the RT cosmo application package/archive

## Proposal #1 - remove daemonize

The RT cosmo application is controlled by the ```rlx3-starter``` as depicted in the figure below. The difference is that the ```daemonize``` package is not used anymore and.

![RT cosmo proposal #1 - components](1_rtcosmo_app_mng_component_proposal1.png)

This solution ends up with the following processes on the system.

![RT cosmo current - process tree](1_rtcosmo_app_mng_tree_proposal1.png)

### Drawbacks
- several process are running on top of the RT cosmo application
- service unit file is separated from the RT cosmo application package/archive

## Proposal #2 - remove rlx3-starter

The RT cosmo application is controlled by ```systemd``` directly as depicted in the figure below.

![RT cosmo proposal #2 - components](2_rtcosmo_app_mng_component_proposal2.png)

This solution ends up with the following processes on the system.

![RT cosmo proposal #2 - process tree](2_rtcosmo_app_mng_tree_proposal2.png)

### Drawbacks
- customer must integrate the service unit file to the RT cosmo application

### Impacts
- the RLX3 starter is completely removed
- ExecStartPre script might be created from scratch
