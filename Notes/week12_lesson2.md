# On Clouds

Cloud computing is not a physical thing, it is a *concept*,
or rather a model for enabling ubiquitous, convenient, on-demand network.
- Essential characteristics:
    1. On-demand self-service
    2. Broad network access
        - access from anywhere
    3. Resource pooling
        - access to large pools of resources
    4. Rapid elasticity
        - Provisioning of resources on-the-fly
        - in other words: flexibility of allocation
    5. Measured service
        - Measure how much has been used.
        - Enables people to be charged fairly.
        
        
- 3 Service Models:
    1. Software as a Service
        - Applications, meant for end users
        - **Capability provided to consumer to use the
        application. Important to note that the consumer
        cannot manage or control any of the underlying
        cloud infrastructure**
        - This should be purely for end-users/clients, 
        using front-end APIs.
        - *Jit's explanation:* anything that uses cloud infra, but does not
        allow us to modify the underlying infra. (Non-programming)
        - examples:
            - emails
            - games
            - Emulators
            - dropbox
    2. Platform as a service
        - looking at tools for deployment.
        - For developers to deploy
        - **Provides suitable runtime environment**
        - Can provide standard **SQL** services
        - Allows access from many machines, with no 
        local installation required.
        - Uses pay-as-you-go, or one-time payment, etc.
        - Any platform that is used to develop something
        meant for other consumers.
        - **Capability provided to the consumer to deploy
        onto the cloud infra consumer-created or acquired
        applications created using programming**
        - Consumer cannot manage or control underlying cloud infra,
        including network, servers, OS, storage.
        - Examples:
            - Database
            - web server
            - execution runtime
            - Google app engine
            - Amazon elastic beanstalk (AWS)
            - Windows Azure
    3. Infrastructure as a service
        - IDEs, for application developers.
        - Designed for system/network architects
        - pay per unit time
        - Cannot control underlying cloud infra
        - **Can control OS, storage, etc**
        - Storage, etc.
        - Examples:
            - AWS
            - Google compute engine
            - Storage
            - Load balancers
            - Firewalls
            
- Slide 30:
    - Dockers/containers vs VMs

| Containers | Virtual Machines |
| --- | --- |
| takes up smaller space | since it stores OS, larger space |
| starts up quickly, like starting an app | starts slowly, like starting a computer |

    
- Handling big data:
    - hadoop
    
- YARN: yet another resource Negotiator

- 3 types of query data:
    1. map
    2. shuffle
    3. reduce

