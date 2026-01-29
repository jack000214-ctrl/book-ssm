# Upgrade Progress

  ### ✅ Generate Upgrade Plan

  ### ✅ Confirm Upgrade Plan

  ### ⏳ Setup Development Environment ...Running
  
  
  > There are uncommitted changes in the project before upgrading, which have been stashed according to user setting "appModernization.uncommittedChangesAction".

  ### ✅ PreCheck
  
  
  <details>
      <summary>[ click to toggle details ]</summary>
  
  - ###
    ### ❗ Precheck - Build project
    
    
    <details>
        <summary>[ click to toggle details ]</summary>
    
    #### Command
    `mvn clean test-compile -q -B -fn`
    
    #### Errors
    - === Config File error     The below errors can be due to missing dependencies. You may have to refer     to the config files provided earlier to solve it.     'errorMessage': Failed to execute goal on project bookims-ssm: Could not resolve dependencies for project com.mybatis:bookims-ssm:war:1.0-SNAPSHOT: The following artifacts could not be resolved: org.springframework:spring-core:jar:5.3.43 (absent), org.springframework:spring-beans:jar:5.3.43 (absent), org.springframework:spring-context:jar:5.3.43 (absent), org.springframework:spring-jdbc:jar:5.3.43 (absent), org.springframework:spring-tx:jar:5.3.43 (absent), org.springframework:spring-web:jar:5.3.43 (absent), org.springframework:spring-webmvc:jar:5.3.43 (absent), org.springframework:spring-test:jar:5.3.43 (absent), commons-fileupload:commons-fileupload:jar:1.6 (absent): org.springframework:spring-core:jar:5.3.43 was not found in https://repo.maven.apache.org/maven2 during a previous attempt. This failure was cached in the local repository and resolution is not reattempted until the update interval of central has elapsed or updates are forced 
      ```
      Failed to execute goal on project bookims-ssm: Could not resolve dependencies for project com.mybatis:bookims-ssm:war:1.0-SNAPSHOT: The following artifacts could not be resolved: org.springframework:spring-core:jar:5.3.43 (absent), org.springframework:spring-beans:jar:5.3.43 (absent), org.springframework:spring-context:jar:5.3.43 (absent), org.springframework:spring-jdbc:jar:5.3.43 (absent), org.springframework:spring-tx:jar:5.3.43 (absent), org.springframework:spring-web:jar:5.3.43 (absent), org.springframework:spring-webmvc:jar:5.3.43 (absent), org.springframework:spring-test:jar:5.3.43 (absent), commons-fileupload:commons-fileupload:jar:1.6 (absent): org.springframework:spring-core:jar:5.3.43 was not found in https://repo.maven.apache.org/maven2 during a previous attempt. This failure was cached in the local repository and resolution is not reattempted until the update interval of central has elapsed or updates are forced
      ```
    </details>
  </details>

  ### ⏳ Setup Development Environment ...Running

  ### ❗ Setup Development Environment
  
  
  <details>
      <summary>[ click to toggle details ]</summary>
  
  #### Errors
  - File c:\Project\SSLife\book-ssm\.github\java-upgrade\20260120002658\plan.md does not exist, please invoke tool #generate\_upgrade\_plan to generate a valid upgrade plan first.
  </details>