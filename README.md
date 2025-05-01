# Face_Recognition
![Static Badge](https://img.shields.io/badge/version-Alpha(A)%200.0.1.0-blue)

## Description 
This repository has been created for the development of a facial recognition application, it continues to be constantly developed and improved.

## Version control
To standardize the updates and way of working, we will work with the Semantic Versioning 2.0.0 versioning system in which the scheme is as follows:
  
  1. Pre_alpha (PreA): Activities performed during the software project before formal testing
  2. Alpha (A): For early development versions that are not stable.
  3. Beta (B): For more stable pre-release versions that are close to the final release.
  4. Release candidate (RC): For final release candidate versions that are about to be published.

  example: 
  PreA 0.0.1.0


## Project Configuration Information

### Diagram
  <pre> ```mermaid graph TD 91["User&lt;br&gt;External Actor"] subgraph 89["Face Recognition System"] 100["Minio Storage&lt;br&gt;Object Storage"] 101["External User/Log API&lt;br&gt;External Service"] 90["Backend API"] 99["MongoDB Database&lt;br&gt;Database"] %% Edges at this level (grouped by source) 90["Backend API"] -->|Reads/Writes embeddings| 99["MongoDB Database&lt;br&gt;Database"] 90["Backend API"] -->|Stores/Retrieves images| 100["Minio Storage&lt;br&gt;Object Storage"] 90["Backend API"] -->|Calls| 101["External User/Log API&lt;br&gt;External Service"] end %% Edges at this level (grouped by source) 91["User&lt;br&gt;External Actor"] -->|Sends image for recognition| 90["Backend API"] ``` </pre>
