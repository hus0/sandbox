# RT cosmo application management aka RLX3 starter

## Overview

The purpose of this document is to create a proposal for the RT cosmo application management /start, stop, restart, etc/.

Find below the current state and the proposals for the RT cosmo application management.

## Current state

The RT cosmo application is managed by ```rlx3-starter``` as depicted in the figure below.

![RT cosmo current - components](0_rtcosmo_app_mng_component_current.png)

Systemd runs RLX3 starter. Afterwards RLX3 starter fires ```start.sh``` script which basically starts the RT cosmo application.

This solution ends up with the following processes on the system.

![RT cosmo current - process tree](0_rtcosmo_app_mng_tree_current.png)

### Drawbacks
- daemonize package is required
- several process are running on top of the RT cosmo application
- service unit file is separated from the RT cosmo application

## Proposal #1 - remove daemonize

The RT cosmo application is managed by ```rlx3-starter``` as depicted in the figure below. The only difference is that the ```daemonize``` package is not used anymore.

![RT cosmo proposal #1 - components](1_rtcosmo_app_mng_component_proposal1.png)

This solution ends up with the following processes on the system.

![RT cosmo current - process tree](1_rtcosmo_app_mng_tree_proposal1.png)

### Drawbacks
- several process are running on top of the RT cosmo application
- service unit file is separated from the RT cosmo application

## Proposal #2 - remove rlx3-starter

The RT cosmo application is managed directly by ```systemd``` as depicted in the figure below.

![RT cosmo proposal #2 - components](2_rtcosmo_app_mng_component_proposal2.png)

This solution ends up with the following processes on the system.

![RT cosmo proposal #2 - process tree](2_rtcosmo_app_mng_tree_proposal2.png)

### Drawbacks
- customer must integrate the service unit file to the RT cosmo application

### Impacts
- rlx3-starter is completely removed
- ExecStartPre script might be created from scratch
