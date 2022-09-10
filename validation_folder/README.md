# Summary statistics for the available dandisets (Updated on 2022-09-05)

## BIDS dandisets

- Total number of BIDS dandisets: 7

- Median number of files in each BIDS dandiset: 17.0

- Median number of bytes in each BIDS dandiset: 6,079,714,780


## NWB dandisets

- Total number of NWB dandisets: 102

- Median number of files in each NWB dandiset: 54.5

- Median number of bytes in each NWB dandiset: 12,161,956,576

- 6 most commonly measured variables: Units, ProcessingModule, ElectrodeGroup, ElectricalSeries, BehavioralTimeSeries, CurrentClampSeries

- NWB dandisets that pass NWBInspector and thus are possibly NWBE compatible: [000005](https://dandiarchive.org/dandiset/000005), [000008](https://dandiarchive.org/dandiset/000008), [000012](https://dandiarchive.org/dandiset/000012), [000013](https://dandiarchive.org/dandiset/000013), [000019](https://dandiarchive.org/dandiset/000019), [000021](https://dandiarchive.org/dandiset/000021), [000027](https://dandiarchive.org/dandiset/000027), [000034](https://dandiarchive.org/dandiset/000034), [000035](https://dandiarchive.org/dandiset/000035), [000043](https://dandiarchive.org/dandiset/000043), [000048](https://dandiarchive.org/dandiset/000048), [000053](https://dandiarchive.org/dandiset/000053), [000056](https://dandiarchive.org/dandiset/000056), [000060](https://dandiarchive.org/dandiset/000060), [000064](https://dandiarchive.org/dandiset/000064), [000067](https://dandiarchive.org/dandiset/000067), [000068](https://dandiarchive.org/dandiset/000068), [000069](https://dandiarchive.org/dandiset/000069), [000107](https://dandiarchive.org/dandiset/000107), [000117](https://dandiarchive.org/dandiset/000117), [000122](https://dandiarchive.org/dandiset/000122), [000126](https://dandiarchive.org/dandiset/000126), [000128](https://dandiarchive.org/dandiset/000128), [000129](https://dandiarchive.org/dandiset/000129), [000130](https://dandiarchive.org/dandiset/000130), [000138](https://dandiarchive.org/dandiset/000138), [000139](https://dandiarchive.org/dandiset/000139), [000140](https://dandiarchive.org/dandiset/000140), [000144](https://dandiarchive.org/dandiset/000144), [000147](https://dandiarchive.org/dandiset/000147), [000148](https://dandiarchive.org/dandiset/000148), [000165](https://dandiarchive.org/dandiset/000165), [000173](https://dandiarchive.org/dandiset/000173), [000212](https://dandiarchive.org/dandiset/000212), [000217](https://dandiarchive.org/dandiset/000217), [000220](https://dandiarchive.org/dandiset/000220), [000221](https://dandiarchive.org/dandiset/000221), [000226](https://dandiarchive.org/dandiset/000226), [000230](https://dandiarchive.org/dandiset/000230), [000232](https://dandiarchive.org/dandiset/000232), [000233](https://dandiarchive.org/dandiset/000233), [000239](https://dandiarchive.org/dandiset/000239), [000245](https://dandiarchive.org/dandiset/000245), [000249](https://dandiarchive.org/dandiset/000249), [000251](https://dandiarchive.org/dandiset/000251), [000292](https://dandiarchive.org/dandiset/000292), [000293](https://dandiarchive.org/dandiset/000293), [000295](https://dandiarchive.org/dandiset/000295), [000296](https://dandiarchive.org/dandiset/000296), [000297](https://dandiarchive.org/dandiset/000297), [000299](https://dandiarchive.org/dandiset/000299)

- NWBE compatibility terminology: 
  - LL-P: Likely plottable - file whose datatypes extend TimeSeries that can be viewed and plotted 
  - LL-V: Likely viewable - file whose datatypes might not extend TimeSeries that can be viewed 
  - NC-0: Not compatible level 0 - file cannot be opened 
  - NC-1: Not compatible level 1 - geppetto model for file cannot be created 
  - NI: No information - file is not tested 

<details><summary> Summary information on the available dandisets (more details in dandiset_summary.csv).
</summary><p>



*[DANDI:000003](https://dandiarchive.org/dandiset/000003/draft)*: **Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells**

- Data type: **Neurodata Without Borders (NWB)**, file count: **101**, total size (MB): **2,559,248.01**

- Species: **House mouse**

- Keywords: **cell types**, **current source density**, **laminar recordings**, **oscillations**, **mossy cells**, **granule cells**, **optogenetics**

- Variables measured: **DecompositionSeries**, **LFP**, **Units**, **Position**, **ElectricalSeries**

- Source paper: *Senzai, Yuta; Fernandez-Ruiz, Antonio; Buzsáki, György (2022) Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000004](https://dandiarchive.org/dandiset/000004/draft)*: **A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **87**, total size (MB): **6,197.47**

- Species: **Human**

- Keywords: **cognitive neuroscience**, **data standardization**, **decision making**, **declarative memory**, **neurophysiology**, **neurosurgery**, **NWB**, **open source**, **single-neurons**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Chandravadia, Nand; Liang, Dehua; Schjetnan, Andrea Gomez Palacio; Carlson, April; Faraut, Mailys; Chung, Jeffrey M.; Reed, Chrystal M.; Dichter, Ben; Maoz, Uri; Kalia, Suneil K.; Valiante, Taufik A.; Mamelak, Adam N.; Rutishauser, Ueli (2022) A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, CRITICAL, BEST_PRACTICE_VIOLATION](000004_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 54.65 MB | 
[File info](https://api.dandiarchive.org/api/assets/a831c980-7b5a-4ad2-9687-7caf5ae27c56) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000004/draft/files?location=sub-P16HMH%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a831c980-7b5a-4ad2-9687-7caf5ae27c56/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 54.68 MB | 
[File info](https://api.dandiarchive.org/api/assets/e22c078c-43d9-4713-84f5-02d2e1db707c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000004/draft/files?location=sub-P15HMH%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e22c078c-43d9-4713-84f5-02d2e1db707c/download/) 
---

*[DANDI:000005](https://dandiarchive.org/dandiset/000005/draft)*: **Electrophysiology data from thalamic and cortical neurons during somatosensation**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **148**, total size (MB): **46,436.69**

- Species: **House mouse**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **OptogeneticSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Yu, Jianing; Gutnisky, Diego A; Hires, S Andrew; Svoboda, Karel (2022) Electrophysiology data from thalamic and cortical neurons during somatosensation*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000005_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 46.54 MB | 
[File info](https://api.dandiarchive.org/api/assets/3ee6887c-1462-4d39-a3f3-e0e356e673d5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000005/draft/files?location=sub-anm266945%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/3ee6887c-1462-4d39-a3f3-e0e356e673d5/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 58.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/b73da40b-a5bf-4f1c-9cfc-479b1ea4d0f3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000005/draft/files?location=sub-anm266951%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/b73da40b-a5bf-4f1c-9cfc-479b1ea4d0f3/download/) 
---

*[DANDI:000006](https://dandiarchive.org/dandiset/000006/draft)*: **Mouse anterior lateral motor cortex (ALM) in delay response task**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0.2**), file count: **53**, total size (MB): **139.6**

- Species: **House mouse**

- Variables measured: **Units**, **ElectrodeGroup**, **BehavioralEvents**

- Source paper: *Economo, Michael N.; Svoboda, Karel (2022) Mouse anterior lateral motor cortex (ALM) in delay response task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000006_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/32cb0ae9-49fd-4bf9-b939-3960df7aeca2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000006/draft/files?location=sub-anm369963%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/32cb0ae9-49fd-4bf9-b939-3960df7aeca2/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 0.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/e949d5c5-ed3d-4e17-9adf-a7facab36870) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000006/draft/files?location=sub-anm372795%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e949d5c5-ed3d-4e17-9adf-a7facab36870/download/) 
---

*[DANDI:000007](https://dandiarchive.org/dandiset/000007/draft)*: **A cortico-cerebellar loop for motor planning**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **54**, total size (MB): **199.44**

- Species: **House mouse**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Gao, Zhenyu; Davis, Courtney; Thomas, Alyse M.; Economo, Michael N.; Abrego, Amada M.; Svoboda, Karel; Zeeuw, Chris I. De; Li, Nuo (2022) A cortico-cerebellar loop for motor planning*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000007_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.54 MB | 
[File info](https://api.dandiarchive.org/api/assets/558d1353-a52e-4d06-a027-cadbbffaa25c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000007/draft/files?location=sub-anm00314758%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/558d1353-a52e-4d06-a027-cadbbffaa25c/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 0.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/c093327c-6a1f-4290-a972-ef9976a48576) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000007/draft/files?location=sub-BAYLORCD13%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/c093327c-6a1f-4290-a972-ef9976a48576/download/) 
---

*[DANDI:000008](https://dandiarchive.org/dandiset/000008/draft)*: **Phenotypic variation within and across transcriptomic cell types in mouse motor cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1328**, total size (MB): **11,922.33**

- Species: **Mus musculus - House mouse**

- Keywords: **Patch-seq**, **cortex**, **motor cortex**, **mouse**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Scala, Federico; Kobak, Dmitry; Bernabucci, Matteo; Bernaerts, Yves; Cadwell, Cathryn Rene; Castro, Jesus Ramon; Hartmanis, Leonard; Jiang, Xiaolong; Laturnus, Sophie; Miranda, Elanine; Mulherkar, Shalaka; Tan, Zheng Huan; Yao, Zizhen; Zeng, Hongkui; Sandberg, Rickard; Berens, Philipp; Tolias, Andreas Savas (2022) Phenotypic variation within and across transcriptomic cell types in mouse motor cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000008_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 3.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/6810513d-2d2e-4ed0-b5b5-f221025d766e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000008/draft/files?location=sub-mouse-KKXUD%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/6810513d-2d2e-4ed0-b5b5-f221025d766e/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 3.25 MB | 
[File info](https://api.dandiarchive.org/api/assets/874c6994-6535-41af-9d20-3a9763fb6df2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000008/draft/files?location=sub-mouse-UALZV%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/874c6994-6535-41af-9d20-3a9763fb6df2/download/) 
---

*[DANDI:000009](https://dandiarchive.org/dandiset/000009/draft)*: **Maintenance of persistent activity in a frontal thalamocortical loop**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **173**, total size (MB): **12,919.71**

- Species: **House mouse**

- Variables measured: **Units**, **ElectrodeGroup**, **ProcessingModule**, **BehavioralTimeSeries**, **CurrentClampStimulusSeries**, **OptogeneticSeries**

- Source paper: *Guo, Zengcai; Inagaki, Hidehiko; Daie, Kayvon; Druckmann, Shaul; Gerfen, Charles R.; Svoboda, Karel (2022) Maintenance of persistent activity in a frontal thalamocortical loop*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000009_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/8ce1a50f-11bd-4a75-a510-64c3f32bb529) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000009/draft/files?location=sub-anm00264942%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/8ce1a50f-11bd-4a75-a510-64c3f32bb529/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 0.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/10f60b99-4286-4780-a767-f0267d877abd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000009/draft/files?location=sub-anm00237800%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/10f60b99-4286-4780-a767-f0267d877abd/download/) 
---

*[DANDI:000010](https://dandiarchive.org/dandiset/000010/draft)*: **A motor cortex circuit for motor planning and movement**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **158**, total size (MB): **40,006.57**

- Species: **House mouse**

- Variables measured: **BehavioralTimeSeries**, **Units**, **ElectrodeGroup**, **BehavioralEvents**, **PlaneSegmentation**

- Source paper: *Li, Nuo; Chen, Tsai-Wen; Guo, Zengcai V.; Gerfen, Charles R.; Svoboda, Karel (2022) A motor cortex circuit for motor planning and movement*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000010_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 26.71 MB | 
[File info](https://api.dandiarchive.org/api/assets/427d4e22-35b3-4775-8d82-f4598ecdcc87) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000010/draft/files?location=sub-217951%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/427d4e22-35b3-4775-8d82-f4598ecdcc87/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 27.77 MB | 
[File info](https://api.dandiarchive.org/api/assets/348c64a2-381a-470b-891d-d5de316b3ad8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000010/draft/files?location=sub-226244%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/348c64a2-381a-470b-891d-d5de316b3ad8/download/) 
---

*[DANDI:000011](https://dandiarchive.org/dandiset/000011/draft)*: **Robust neuronal dynamics in premotor cortex during motor planning**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **92**, total size (MB): **32,435.33**

- Species: **House mouse**

- Variables measured: **BehavioralEvents**, **ElectrodeGroup**, **Units**, **BehavioralTimeSeries**

- Source paper: *Li, Nuo; Daie, Kayvon; Svoboda, Karel; Druckmann, Shaul (2022) Robust neuronal dynamics in premotor cortex during motor planning*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000011_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 89.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/354d36fd-fa87-4bc4-adaf-ba5b846d38ef) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000011/draft/files?location=sub-291064%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/354d36fd-fa87-4bc4-adaf-ba5b846d38ef/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 164.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/bc019955-f5d3-4fec-ab7a-e01ed12f493b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000011/draft/files?location=sub-291063%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/bc019955-f5d3-4fec-ab7a-e01ed12f493b/download/) 
---

*[DANDI:000012](https://dandiarchive.org/dandiset/000012/draft)*: **Kriegstein2020**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **297**, total size (MB): **487.52**

- Species: **Human**

- Variables measured: **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Zhou, Li; Kriegstein, Arnold (2022) Kriegstein2020*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000012_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.26 MB | 
[File info](https://api.dandiarchive.org/api/assets/06a78426-1ea5-4a66-b4df-3fb112387dc5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000012/draft/files?location=sub-2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/06a78426-1ea5-4a66-b4df-3fb112387dc5/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 0.47 MB | 
[File info](https://api.dandiarchive.org/api/assets/82eaa51c-c79f-4219-bc06-b0aa330ccbce) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000012/draft/files?location=sub-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/82eaa51c-c79f-4219-bc06-b0aa330ccbce/download/) 
---

*[DANDI:000013](https://dandiarchive.org/dandiset/000013/draft)*: **Low-noise encoding of active touch by layer 4 in the somatosensory cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **52**, total size (MB): **11,408.74**

- Species: **House mouse**

- Variables measured: **BehavioralTimeSeries**, **CurrentClampSeries**, **PatchClampSeries**

- Source paper: *Hires, Samuel; Gutnisky, Diego; Yu, Jianing; O'Connor, Daniel H; Svoboda, Karel (2022) Low-noise encoding of active touch by layer 4 in the somatosensory cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000013_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 47.98 MB | 
[File info](https://api.dandiarchive.org/api/assets/061d6422-018a-4fe0-b914-119b9297be7d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000013/draft/files?location=sub-anm244024%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/061d6422-018a-4fe0-b914-119b9297be7d/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 59.92 MB | 
[File info](https://api.dandiarchive.org/api/assets/b8b1b393-e001-452f-b48f-a7b78b09a582) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000013/draft/files?location=sub-anm266945%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/b8b1b393-e001-452f-b48f-a7b78b09a582/download/) 
---

*[DANDI:000015](https://dandiarchive.org/dandiset/000015/draft)*: **A Map of Anticipatory Activity in Mouse Motor Cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **210**, total size (MB): **17,159.73**

- Species: **House mouse**

- Variables measured: **BehavioralEvents**, **PlaneSegmentation**

- Source paper: *Chen, Tsai-Wen; Li, Nuo; Daie, Kayvon; Svoboda, Karel (2022) A Map of Anticipatory Activity in Mouse Motor Cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000015_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 16.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/70c2d486-4f4b-4821-9f37-540cb1e28de2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000015/draft/files?location=sub-an044%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/70c2d486-4f4b-4821-9f37-540cb1e28de2/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 30.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/72138f7e-5f52-43f8-be08-8cd608764166) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000015/draft/files?location=sub-an043%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/72138f7e-5f52-43f8-be08-8cd608764166/download/) 
---

*[DANDI:000016](https://dandiarchive.org/dandiset/000016/draft)*: **Excitatory and inhibitory subnetworks are equally selective during decision-making and emerge simultaneously during learning**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **135**, total size (MB): **62,572.04**

- Variables measured: **BehavioralTimeSeries**, **PlaneSegmentation**

- Source paper: *Najafi, Farzaneh; Churchland, Anne K. (2022) Excitatory and inhibitory subnetworks are equally selective during decision-making and emerge simultaneously during learning*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000016_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 199.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/913646f8-4d02-45f5-b830-85dfc69ae74a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000016/draft/files?location=sub-mouse2-fni17%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/913646f8-4d02-45f5-b830-85dfc69ae74a/download/) 
- NWBE compatibility - file 2: NC-1  
Size: 214.5 MB | 
[File info](https://api.dandiarchive.org/api/assets/b24bfa76-2a06-440f-9b3a-8e06de9ce493) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000016/draft/files?location=sub-mouse1-fni16%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/b24bfa76-2a06-440f-9b3a-8e06de9ce493/download/) 
---

*[DANDI:000017](https://dandiarchive.org/dandiset/000017/draft)*: **Distributed coding of choice, action and engagement across the mouse brain**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **39**, total size (MB): **14,682.59**

- Species: **House mouse**

- Keywords: **neuropixels**

- Variables measured: **ProcessingModule**, **PupilTracking**, **BehavioralEpochs**, **Units**, **BehavioralEvents**, **BehavioralTimeSeries**, **ElectrodeGroup**

- Source paper: *Steinmetz, Nicholas; Zatka-Haas, Peter; Carandini, Matteo; Harris, Kenneth; Wang, Renee (2022) Distributed coding of choice, action and engagement across the mouse brain*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, CRITICAL, BEST_PRACTICE_VIOLATION](000017_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 216.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/3722e6b8-d47f-4feb-a9ae-9c368e41166b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000017/draft/files?location=sub-Lederberg%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/3722e6b8-d47f-4feb-a9ae-9c368e41166b/download/) 
- NWBE compatibility - file 2: NC-1  
Size: 272.08 MB | 
[File info](https://api.dandiarchive.org/api/assets/9a19c19e-c91d-4d3c-ac97-ad98c621634f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000017/draft/files?location=sub-Richards%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/9a19c19e-c91d-4d3c-ac97-ad98c621634f/download/) 
---

*[DANDI:000018](https://dandiarchive.org/dandiset/000018/draft)*: **Mouse Spinal Cord Ephys Dataset**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Tao, Can; Zhang, Guang-Wei (2022) Mouse Spinal Cord Ephys Dataset*

---

*[DANDI:000019](https://dandiarchive.org/dandiset/000019/draft)*: **Human ECoG speaking consonant-vowel syllables**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0.2**), file count: **31**, total size (MB): **55,585.86**

- Species: **Human**

- Keywords: **electrocorticography (ECoG)**, **speech production**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**, **ProcessingModule**, **Spectrum**

- Source paper: *Bouchard, Kristofer E.; Chang, Edward F. (2022) Human ECoG speaking consonant-vowel syllables*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000019_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 1099.89 MB | 
[File info](https://api.dandiarchive.org/api/assets/fbd3bc15-d716-495f-814d-1aa14f8d3b45) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000019/draft/files?location=sub-GP31%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/fbd3bc15-d716-495f-814d-1aa14f8d3b45/download/) 
- NWBE compatibility - file 2: NI  
Size: 1551.06 MB | 
[File info](https://api.dandiarchive.org/api/assets/911776e7-aebc-4206-b8f3-01f66c7bf747) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000019/draft/files?location=sub-GP33%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/911776e7-aebc-4206-b8f3-01f66c7bf747/download/) 
---

*[DANDI:000020](https://dandiarchive.org/dandiset/000020/draft)*: **Patch-seq recordings from mouse visual cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **4435**, total size (MB): **141,856.44**

- Species: **House mouse**

- Keywords: **Patch-seq**, **mouse**, **visual cortex**, **interneuron**

- Variables measured: **ProcessingModule**

- Source paper: *Allen Institute for Brain Science (2022) Patch-seq recordings from mouse visual cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION](000020_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 11.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/17f31e2b-26b4-4c3e-8e98-423769cc3912) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000020/draft/files?location=sub-639391596%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/17f31e2b-26b4-4c3e-8e98-423769cc3912/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 12.05 MB | 
[File info](https://api.dandiarchive.org/api/assets/df0ed794-e7b5-45a0-9f7f-5aa75e70348d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000020/draft/files?location=sub-643830482%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/df0ed794-e7b5-45a0-9f7f-5aa75e70348d/download/) 
---

*[DANDI:000021](https://dandiarchive.org/dandiset/000021/draft)*: **20191003_AIBS_mouse_ecephys_brain_observatory_1_1**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **214**, total size (MB): **477,562.34**

- Species: **House mouse**

- Keywords: **electrophysiology**, **life sciences**, **machine learning**, **neurobiology**, **signal processing**

- Variables measured: **ProcessingModule**, **LFP**, **Units**

- Source paper: *Siegle, Josh; Wakeman, Wayne; Jia, Xiaoxuan; Heller, Gregg; Ramirez, Tamina; Graddis, Nile; Mei, Nicholas; Durand, Severine (2022) 20191003_AIBS_mouse_ecephys_brain_observatory_1_1*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000021_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 72.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/4d5f1bda-3d20-46f0-a0c8-20f3a3ee9d54) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000021/draft/files?location=sub-703279277%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/4d5f1bda-3d20-46f0-a0c8-20f3a3ee9d54/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 898.78 MB | 
[File info](https://api.dandiarchive.org/api/assets/e1f0127e-f5d7-4cac-a42c-bb76127f2ddc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000021/draft/files?location=sub-719828686%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e1f0127e-f5d7-4cac-a42c-bb76127f2ddc/download/) 
---

*[DANDI:000022](https://dandiarchive.org/dandiset/000022/draft)*: **20191003_AIBS_mouse_ecephys_functional_connectivity**

- Data type: **Neurodata Without Borders (NWB)**, file count: **169**, total size (MB): **374,956.84**

- Species: **House mouse**

- Keywords: **electrophysiology**, **life sciences**, **machine learning**, **neurobiology**, **signal processing**

- Variables measured: **LFP**, **ProcessingModule**, **Units**

- Source paper: *Siegle, Josh; Wakeman, Wayne; Jia, Xiaoxuan; Durand, Severine; Heller, Gregg; Ramirez, Tamina; Graddis, Nile; Mei, Nicholas (2022) 20191003_AIBS_mouse_ecephys_functional_connectivity*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000023](https://dandiarchive.org/dandiset/000023/draft)*: **Patch-seq recordings from human cortex (June 2020)**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **318**, total size (MB): **12,401.58**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortex**, ** layer 2/3**

- Variables measured: **ProcessingModule**

- Source paper: *Allen Institute for Brian Science (2022) Patch-seq recordings from human cortex (June 2020)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000023_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 13.5 MB | 
[File info](https://api.dandiarchive.org/api/assets/7687363f-dd32-4325-9f40-705227fd470c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000023/draft/files?location=sub-695464588%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7687363f-dd32-4325-9f40-705227fd470c/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 14.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/20991256-4a71-48bb-ae0a-e4ccaf29a192) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000023/draft/files?location=sub-731978186%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/20991256-4a71-48bb-ae0a-e4ccaf29a192/download/) 
---

*[DANDI:000024](https://dandiarchive.org/dandiset/000024/draft)*: **LFP & MUA from BF**

, file count: **0**, total size (MB): **0.0**

- Keywords: **LFP, BF, interhemispheric**

- Source paper: *LFP & MUA from BF (2022).*

---

*[DANDI:000025](https://dandiarchive.org/dandiset/000025/draft)*: **Example intracellular ephys data from LNMC & BBP**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1**, total size (MB): **13.66**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **VoltageClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Example intracellular ephys data from LNMC & BBP (2022).*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: UNABLE

---

*[DANDI:000026](https://dandiarchive.org/dandiset/000026/draft)*: **Human brain cell census for BA 44/45**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **40471**, total size (MB): **11,752,241.72**

- Keywords: **multi-modal imaging**, **MRI**, **OCT**, **SPIM**, **human cortex**, **Broca's area**, **Motor cortex**, **Stereology**

- Variables measured: 

- Source paper: *Mazzamuto, Giacomo; Costantini, Irene; Gavryusev, Vladislav; Castelli, Filippo Maria; Pesce, Luca; Scardigli, Marina; Pavone, Francesco Saverio; Roffilli, Matteo; Silvestri, Ludovico; Brady, Niamh; Ramazzotti, Josephine; Hof, Patrick R.; Boas, David A.; Fischl, Bruce; Morgan, Leah; Yang, Jiarui; Chang, Shuaibin; Laffey, Jessie; Magnain, Caroline; Varadarajan, Divya; Wang, Hui; Frost, Robert; Kouwe, Andre van der; Player, Allison Stevens; Atzeni, Alessia; Gonzalez, Juan Eugenio Iglesias; Balbastre, Yael; Vera, Matthew; Cordero, Devani; Nestor, Kimberly; Ammon, William; Nolan, Jackson; Mora, Jocelyn; Pallares, Erendira Garcia; Augustinack, Jean; Diamond, Bram; Fogarty, Morgan; Boyd, Emma; Varghese, Merina; Dalca, Adrian V.; Edlow, Brian; Frosche, Matthew; Wicinski, Bridget; Chen, I-Chun Anderson (2022) Human brain cell census for BA 44/45*

---

*[DANDI:000027](https://dandiarchive.org/dandiset/000027/draft)*: **Test dataset for testing dandi-cli.**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0b**), file count: **1**, total size (MB): **0.02**

- Species: **Brown rat**

- Keywords: **development**

- Variables measured: 

- Source paper: *Halchenko, Yaroslav O. (2022) Test dataset for testing dandi-cli*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000027_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.02 MB | 
[File info](https://api.dandiarchive.org/api/assets/1c095f5f-d1e2-45db-b807-fdcfea08c6de) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000027/draft/files?location=sub-RAT123%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/1c095f5f-d1e2-45db-b807-fdcfea08c6de/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000028](https://dandiarchive.org/dandiset/000028/draft)*: **Simulated cortical Neuropixels recording with ground truth**

- Data type: **Neurodata Without Borders (NWB)**, file count: **3**, total size (MB): **42,942.23**

- Species: **House mouse**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**, **Units**

- Source paper: *Simulated cortical Neuropixels recording with ground truth (2022).*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000029](https://dandiarchive.org/dandiset/000029/draft)*: **Test dataset for development purposes**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0.2**), file count: **5**, total size (MB): **20.72**

- Species: **House mouse**

- Keywords: **development**

- Variables measured: **BehavioralEvents**, **ElectrodeGroup**, **Units**

- Source paper: *Last, First (2022) Test dataset for development purposes*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000029_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.02 MB | 
[File info](https://api.dandiarchive.org/api/assets/86e09d7e-4355-4887-9c5a-7a137c046953) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000029/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/86e09d7e-4355-4887-9c5a-7a137c046953/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 6.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/38f2024d-62a9-4c79-8a22-7a0ff34b331d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000029/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/38f2024d-62a9-4c79-8a22-7a0ff34b331d/download/) 
---

*[DANDI:000030](https://dandiarchive.org/dandiset/000030/draft)*: **Allen Brain Observatory Neuropixels recording**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Allen Brain Observatory Neuropixels recording (2022).*

---

*[DANDI:000031](https://dandiarchive.org/dandiset/000031/draft)*: **ABC**

, file count: **0**, total size (MB): **0.0**

- Source paper: *ABC (2022).*

---

*[DANDI:000032](https://dandiarchive.org/dandiset/000032/draft)*: **Test dataset**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test dataset (2022).*

---

*[DANDI:000033](https://dandiarchive.org/dandiset/000033/draft)*: **Test-2 dataset**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test-2 dataset (2022).*

---

*[DANDI:000034](https://dandiarchive.org/dandiset/000034/draft)*: **SpikeInterface, a unified framework for spike sorting**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **6**, total size (MB): **74,351.01**

- Species: **House mouse**

- Keywords: **Spike Sorting**, **extracellular electrophysiology**

- Variables measured: **ElectrodeGroup**, **Units**, **ElectricalSeries**

- Source paper: *Buccino, Alessio; Hurwitz, Cole; Garcia, Samuel; Magland, Jeremy; Siegle, Joshua; Hurwitz, Roger; Hennig, Matthias H. (2022) SpikeInterface, a unified framework for spike sorting*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000034_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 11.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/c696fc2b-d2e6-4e27-8775-01657193c4a2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000034/draft/files?location=sub-mouse412804%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/c696fc2b-d2e6-4e27-8775-01657193c4a2/download/) 
- NWBE compatibility - file 2: NI  
Size: 6470.91 MB | 
[File info](https://api.dandiarchive.org/api/assets/9822a813-0dec-4d07-810b-1c13341c168d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000034/draft/files?location=sub-P29-16-05-14-retina02-left%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/9822a813-0dec-4d07-810b-1c13341c168d/download/) 
---

*[DANDI:000035](https://dandiarchive.org/dandiset/000035/draft)*: **Temperature-controlled intracellular Patch-seq recordings in mouse motor cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **185**, total size (MB): **1,656.17**

- Species: **House mouse**

- Keywords: **Patch-seq**, **mouse**, **cortex**, **motor cortex**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Scala, Federico; Kobak, Dmitry; Bernabucci, Matteo; Bernaerts, Yves; Cadwell, Cathryn Rene; Castro, Jesus Ramon; Hartmanis, Leonard; Jiang, Xiaolong; Laturnus, Sophie; Miranda, Elanine; Mulherkar, Shalaka; Tan, Zheng Huan; Yao, Zizhen; Last, First; Zeng, Hongkui; Sandberg, Rickard; Berens, Philipp; Tolias, Andreas Savas (2022) Temperature-controlled intracellular Patch-seq recordings in mouse motor cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000035_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 4.63 MB | 
[File info](https://api.dandiarchive.org/api/assets/f1fe5b46-ca4d-4884-83e1-25e3b008bdb2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000035/draft/files?location=sub-mouse-WPOGH%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/f1fe5b46-ca4d-4884-83e1-25e3b008bdb2/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 5.69 MB | 
[File info](https://api.dandiarchive.org/api/assets/d3f3b662-45ee-4c14-88b5-2c96caa28b9a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000035/draft/files?location=sub-mouse-MITSU%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d3f3b662-45ee-4c14-88b5-2c96caa28b9a/download/) 
---

*[DANDI:000036](https://dandiarchive.org/dandiset/000036/draft)*: **Allen Institute Openscope - Meaningful project**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **57**, total size (MB): **79,771.34**

- Keywords: **two photon imaging**

- Variables measured: **BehavioralTimeSeries**, **PlaneSegmentation**

- Source paper: *Last, First (2022) Allen Institute Openscope - Meaningful project*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000036_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 1306.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/3ff75d8e-318f-47d1-805a-1b409b1600e2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000036/draft/files?location=sub-406876%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/3ff75d8e-318f-47d1-805a-1b409b1600e2/download/) 
- NWBE compatibility - file 2: NC-1  
Size: 1310.77 MB | 
[File info](https://api.dandiarchive.org/api/assets/3988673a-e876-4a0e-83c3-12dc35229a7f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000036/draft/files?location=sub-389014%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/3988673a-e876-4a0e-83c3-12dc35229a7f/download/) 
---

*[DANDI:000037](https://dandiarchive.org/dandiset/000037/draft)*: **Allen Institute Openscope - Credit Assignment project**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **96**, total size (MB): **115,953.0**

- Species: **Mus musculus - House mouse**

- Keywords: **learning**, **neocortex**, **pyramidal neurons**, **distal apical dendrites**, **somata**, **L2/3**, **L5**, **two-photon calcium imaging**, **mouse VisP**, **prediction**, **credit assignment**

- Variables measured: **BehavioralTimeSeries**, **PlaneSegmentation**, **PupilTracking**

- Source paper: *Gillon, Colleen J.; Lecoq, Jérôme A.; Zylberberg, Joel; Richards, Blake A. (2022) Allen Institute Openscope - Credit Assignment project*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR, PYNWB_VALIDATION](000037_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 148.63 MB | 
[File info](https://api.dandiarchive.org/api/assets/95d9a0df-d747-48d1-983d-823b76f2c014) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000037/draft/files?location=sub-418779%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/95d9a0df-d747-48d1-983d-823b76f2c014/download/) 
- NWBE compatibility - file 2: NC-1  
Size: 204.78 MB | 
[File info](https://api.dandiarchive.org/api/assets/e5fd108f-5777-43de-aa26-ce152ab02198) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000037/draft/files?location=sub-411771%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e5fd108f-5777-43de-aa26-ce152ab02198/download/) 
---

*[DANDI:000038](https://dandiarchive.org/dandiset/000038/draft)*: **Testytest**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Testytest (2022).*

---

*[DANDI:000039](https://dandiarchive.org/dandiset/000039/draft)*: **Allen Institute – Contrast tuning in mouse visual cortex with calcium imaging**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **100**, total size (MB): **22,607.25**

- Species: **House mouse**

- Keywords: **vision**, **visual cortex**, **inhibition**, **inhibitory circuits**, **circuit dynamics**, **gain control**

- Variables measured: **Units**, **PlaneSegmentation**, **TwoPhotonSeries**, **BehavioralTimeSeries**

- Source paper: *Millman, Dan; Vries, Saskia de (2022) Allen Institute – Contrast tuning in mouse visual cortex with calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000039_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 31.31 MB | 
[File info](https://api.dandiarchive.org/api/assets/645adfe1-7fdf-48f0-9c61-304df785e92d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000039/draft/files?location=sub-664605504%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/645adfe1-7fdf-48f0-9c61-304df785e92d/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 31.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/7b8def8d-69aa-44e3-be02-057c8f1864f0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000039/draft/files?location=sub-678530120%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7b8def8d-69aa-44e3-be02-057c8f1864f0/download/) 
---

*[DANDI:000040](https://dandiarchive.org/dandiset/000040/draft)*: **Neuropixels recordings in mouse visual system**

, file count: **0**, total size (MB): **0.0**

- Keywords: **Neuropixels**

- Source paper: *Jia, Xiaoxuan; Siegle, Josh; Durand, Severine; Heller, Gregg; Ramirez, Tamina (2022) Neuropixels recordings in mouse visual system*

---

*[DANDI:000041](https://dandiarchive.org/dandiset/000041/draft)*: **Network Homeostasis and State Dynamics of Neocortical Sleep**

- Data type: **Neurodata Without Borders (NWB)**, file count: **22**, total size (MB): **154,863.46**

- Species: **Brown rat**

- Keywords: **Firing patterns**, **Sleep/awake states**, **Sleep stages**, **Homeostasis**

- Variables measured: **Units**, **LFP**, **ElectricalSeries**

- Source paper: *Watson, Brendon O.; Levenstein, Daniel; Greene, J. Palmer; Gelinas, Jennifer N.; Buzsáki, György (2022) Network Homeostasis and State Dynamics of Neocortical Sleep*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000042](https://dandiarchive.org/dandiset/000042/draft)*: **Allen Institute Openscope - Meaningful project  - Full movies**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Allen Institute Openscope - Meaningful project  - Full movies (2022).*

---

*[DANDI:000043](https://dandiarchive.org/dandiset/000043/draft)*: **Human, macaque, and mouse L5 pyramidal neuron physiology**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.4**), file count: **94**, total size (MB): **3,271.28**

- Species: **House mouse**

- Keywords: **Patch-seq**, **Motor cortex**, **Betz cell**, **Human**, **Macaque**, **Mouse**

- Variables measured: 

- Source paper: *Kalmbach, Brian; Ting, Jonathan; Owen, Scott; Lein, Ed (2022) Human, macaque, and mouse L5 pyramidal neuron physiology*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000043_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 14.76 MB | 
[File info](https://api.dandiarchive.org/api/assets/26f67672-5162-4f43-86cb-402aed8c582d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000043/draft/files?location=sub-M19-01-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/26f67672-5162-4f43-86cb-402aed8c582d/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 16.17 MB | 
[File info](https://api.dandiarchive.org/api/assets/d715f810-df3f-42b4-8650-e0c64a236ac1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000043/draft/files?location=sub-Q19-26-018%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d715f810-df3f-42b4-8650-e0c64a236ac1/download/) 
---

*[DANDI:000044](https://dandiarchive.org/dandiset/000044/draft)*: **Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences**

- Data type: **Neurodata Without Borders (NWB)**, file count: **8**, total size (MB): **65,708.92**

- Species: **Brown rat**

- Variables measured: **ElectricalSeries**, **LFP**, **Units**

- Source paper: *Grosmark, Andres D.; Buzsáki, György (2022) Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000045](https://dandiarchive.org/dandiset/000045/draft)*: **IBL behavioral data**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **6615**, total size (MB): **97,844.92**

- Species: **House mouse**

- Keywords: **International Brain Laboratory**

- Variables measured: **BehavioralTimeSeries**, **ProcessingModule**, **DecompositionSeries**, **Position**, **ElectrodeGroup**

- Source paper: *International Brain Laboratory (2022) IBL behavioral data*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000045_validation.txt) 

- NWBE compatibility - file 1: NC-0  
Size: 0.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/7946c765-52e4-44e2-90ae-9652f8a956e2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000045/draft/files?location=sub-354e6122-de4a-4945-bafd-d46df65768f6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7946c765-52e4-44e2-90ae-9652f8a956e2/download/) 
- NWBE compatibility - file 2: NC-0  
Size: 0.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/3d982a78-0f0d-4313-a9ed-60a9bdf42db9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000045/draft/files?location=sub-00778394-c956-408d-8a6c-ca3b05a611d5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/3d982a78-0f0d-4313-a9ed-60a9bdf42db9/download/) 
---

*[DANDI:000046](https://dandiarchive.org/dandiset/000046/draft)*: **asdf**

, file count: **0**, total size (MB): **0.0**

- Source paper: *asdf (2022).*

---

*[DANDI:000047](https://dandiarchive.org/dandiset/000047/draft)*: **Test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test (2022).*

---

*[DANDI:000048](https://dandiarchive.org/dandiset/000048/draft)*: **Electrical and optical physiology in in vivo population-scale two-photon calcium imaging**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1**, total size (MB): **590.27**

- Variables measured: **PlaneSegmentation**, **TwoPhotonSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Ledochowitsch, Peter; Huang, Lawrence; Knoblich, Ulf; Oliver, Michael; Lecoq, Jerome; Reid, Clay; Li, Lu; Zeng, Hongkui; Koch, Christof; Waters, Jack; Vries, Saskia E.J. de; Buice, Michael A. (2022) Electrical and optical physiology in in vivo population-scale two-photon calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000048_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 590.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/827b4c2f-4235-4350-b40f-02e120211dcd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000048/draft/files?location=sub-222549%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/827b4c2f-4235-4350-b40f-02e120211dcd/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000049](https://dandiarchive.org/dandiset/000049/draft)*: **Allen Institute – TFxSF tuning in mouse visual cortex with calcium imaging**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **78**, total size (MB): **22,211.89**

- Species: **House mouse**

- Keywords: **Mouse**

- Variables measured: **TwoPhotonSeries**, **Units**, **PlaneSegmentation**, **BehavioralTimeSeries**

- Source paper: *Millman, Daniel; de Vries, Saskia (2022) Allen Institute – TFxSF tuning in mouse visual cortex with calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000049_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 33.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/38cf16f0-0f4c-44ec-b04e-0b0c0b02781b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000049/draft/files?location=sub-760940732%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/38cf16f0-0f4c-44ec-b04e-0b0c0b02781b/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 50.59 MB | 
[File info](https://api.dandiarchive.org/api/assets/7f81af9c-fab1-4a4a-9ca6-992bbbb0a4b3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000049/draft/files?location=sub-759066288%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7f81af9c-fab1-4a4a-9ca6-992bbbb0a4b3/download/) 
---

*[DANDI:000050](https://dandiarchive.org/dandiset/000050/draft)*: **Allen Institute - Run Tuning in the Mouse Visual Cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **56**, total size (MB): **26,372.58**

- Species: **House mouse**

- Variables measured: **TwoPhotonSeries**, **Units**, **PlaneSegmentation**, **BehavioralTimeSeries**

- Source paper: *Allen Institute - Run Tuning in the Mouse Visual Cortex (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000050_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 94.81 MB | 
[File info](https://api.dandiarchive.org/api/assets/f3de94e9-6af4-4169-b911-1e7028ca2021) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000050/draft/files?location=sub-673580710%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/f3de94e9-6af4-4169-b911-1e7028ca2021/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 155.38 MB | 
[File info](https://api.dandiarchive.org/api/assets/55583159-e897-4b77-8a81-48c78e8b6227) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000050/draft/files?location=sub-753847689%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/55583159-e897-4b77-8a81-48c78e8b6227/download/) 
---

*[DANDI:000051](https://dandiarchive.org/dandiset/000051/draft)*: **pons8-yo_16xdownsampled**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1**, total size (MB): **585.93**

- Species: **Human**

- Variables measured: 

- Source paper: *pons8-yo_16xdownsampled (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000051_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 585.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/203fdd15-60d6-41c4-b964-3439163e4e3a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000051/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/203fdd15-60d6-41c4-b964-3439163e4e3a/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000052](https://dandiarchive.org/dandiset/000052/draft)*: **Pons8-BIDS-16xdownsampled**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **518**, total size (MB): **226.8**

- Variables measured: 

- Source paper: *Pons8-BIDS-16xdownsampled (2022).*

---

*[DANDI:000053](https://dandiarchive.org/dandiset/000053/draft)*: **Recordings from medial entorhinal cortex during linear track and open exploration**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **359**, total size (MB): **1,393,128.77**

- Species: **House mouse**

- Keywords: **neuropixel**, **entorhinal cortex**

- Variables measured: **LFP**, **Position**, **Units**, **ElectrodeGroup**, **EyeTracking**, **SpatialSeries**, **ProcessingModule**

- Source paper: *Mallory, Caitlin S.; Hardcastle, Kiah; Campbell, Malcolm G.; Attinger, Alexander; Low, Isabel I. C.; Raymond, Jennifer L.; Giocomo, Lisa M. (2022) Recordings from medial entorhinal cortex during linear track and open exploration*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000053_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 2.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/cefaf356-0f24-4ebb-8970-3ca91d97b405) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000053/draft/files?location=sub-Ella%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/cefaf356-0f24-4ebb-8970-3ca91d97b405/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 2.48 MB | 
[File info](https://api.dandiarchive.org/api/assets/fcce9de1-149d-4ab3-b3a8-9803239fa70a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000053/draft/files?location=sub-Barbara%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/fcce9de1-149d-4ab3-b3a8-9803239fa70a/download/) 
---

*[DANDI:000054](https://dandiarchive.org/dandiset/000054/draft)*: **Plitt & Giocomo (2021) Experience Dependent Contextual Codes in the Hippocampus. Nat Neuro**

- Data type: **Neurodata Without Borders (NWB)**, file count: **85**, total size (MB): **1,959,122.44**

- Species: **House mouse**

- Variables measured: **PlaneSegmentation**, **TwoPhotonSeries**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Plitt, Mark; Giocomo, Lisa M. (2022) Plitt & Giocomo (2021) Experience Dependent Contextual Codes in the Hippocampus. Nat Neuro*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000055](https://dandiarchive.org/dandiset/000055/draft)*: **AJILE12: Long-term naturalistic human intracranial neural recordings and pose**

- Data type: **Neurodata Without Borders (NWB)**, file count: **55**, total size (MB): **845,869.7**

- Species: **Human**

- Variables measured: **Position**, **ProcessingModule**, **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Peterson, Steven M.; Singh, Satpreet H.; Dichter, Benjamin; Scheid, Micheal; Rao, Rajesh P. N.; Brunton, Bingni W. (2022) AJILE12: Long-term naturalistic human intracranial neural recordings and pose*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000056](https://dandiarchive.org/dandiset/000056/draft)*: **Internally organized mechanisms of the head direction sense**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **40**, total size (MB): **207,733.01**

- Species: **House mouse**

- Keywords: ****

- Variables measured: **ElectricalSeries**, **Units**, **LFP**, **Position**, **ProcessingModule**

- Source paper: *Peyrache, Adrien; Lacroix, Marie M; Petersen, Peter C; Buzsáki, György (2022) Internally organized mechanisms of the head direction sense*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000056_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 1306.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/ada02790-6eb6-48ee-902d-9ba017303586) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000056/draft/files?location=sub-Mouse24%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/ada02790-6eb6-48ee-902d-9ba017303586/download/) 
- NWBE compatibility - file 2: NI  
Size: 1892.07 MB | 
[File info](https://api.dandiarchive.org/api/assets/748aa5de-c0de-4aa7-a7ef-2aad2f87a7eb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000056/draft/files?location=sub-Mouse20%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/748aa5de-c0de-4aa7-a7ef-2aad2f87a7eb/download/) 
---

*[DANDI:000057](https://dandiarchive.org/dandiset/000057/draft)*: **foobar**

, file count: **0**, total size (MB): **0.0**

- Source paper: *foobar (2022).*

---

*[DANDI:000058](https://dandiarchive.org/dandiset/000058/draft)*: **MITU01 Dataset**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **17**, total size (MB): **35,328.36**

- Variables measured: 

- Source paper: *MITU01 Dataset (2022).*

---

*[DANDI:000059](https://dandiarchive.org/dandiset/000059/draft)*: **Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies**

- Data type: **Neurodata Without Borders (NWB)**, file count: **54**, total size (MB): **3,261,512.04**

- Species: **Brown rat**

- Variables measured: **SpatialSeries**, **Position**, **LFP**, **Units**, **ProcessingModule**

- Source paper: *Petersen, Peter; Buzsáki, György (2022) Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000060](https://dandiarchive.org/dandiset/000060/draft)*: **Dataset for Finkelstein, Fontolan et al. "Attractor dynamics gate cortical information flow during decision-making"**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **98**, total size (MB): **1,009.09**

- Species: **House mouse**

- Keywords: **motor cortex**, **extracellular electrophysiology**, **decision-making**, **attractor**, **optogenetic stimulation**

- Variables measured: **Units**, **BehavioralEvents**

- Source paper: *Finkelstein, Arseny; Svoboda, Karel (2022) Dataset for Finkelstein, Fontolan et al. "Attractor dynamics gate cortical information flow during decision-making"*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000060_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 1.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/1ecaa50a-5751-46ae-9fef-5e381472b108) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000060/draft/files?location=sub-353938%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/1ecaa50a-5751-46ae-9fef-5e381472b108/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 1.98 MB | 
[File info](https://api.dandiarchive.org/api/assets/f2dd0e64-2c91-4ef6-92b8-84dd3141119e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000060/draft/files?location=sub-365942%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/f2dd0e64-2c91-4ef6-92b8-84dd3141119e/download/) 
---

*[DANDI:000061](https://dandiarchive.org/dandiset/000061/draft)*: **Reactivations of emotional memory in the hippocampus–amygdala system during sleep**

- Data type: **Neurodata Without Borders (NWB)**, file count: **40**, total size (MB): **1,952,634.65**

- Species: **Brown rat**

- Variables measured: **Units**, **LFP**, **ElectricalSeries**, **ProcessingModule**

- Source paper: *Girardeau, Gabrielle; Inema, Ingrid; Buzsáki, György (2022) Reactivations of emotional memory in the hippocampus–amygdala system during sleep*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000063](https://dandiarchive.org/dandiset/000063/draft)*: **UHN_human_heterogeneity**

, file count: **0**, total size (MB): **0.0**

- Source paper: *UHN_human_heterogeneity (2022).*

---

*[DANDI:000064](https://dandiarchive.org/dandiset/000064/draft)*: **Simulation extension example**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1**, total size (MB): **218.37**

- Variables measured: 

- Source paper: *Simulation extension example (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000064_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 218.37 MB | 
[File info](https://api.dandiarchive.org/api/assets/bb61e86d-e28f-4da7-b07a-44dfa377cf32) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000064/draft/files?location=sub-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/bb61e86d-e28f-4da7-b07a-44dfa377cf32/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000065](https://dandiarchive.org/dandiset/000065/draft)*: **Polymer probe recordings from hippocampus (LFP), OFC, NAc, and mPFC**

, file count: **1**, total size (MB): **237,685.09**

- Keywords: **rat, **, **polymer probe**, **electrophysiology**, **nucleus accumbens**, **medial prefrontal cortex**, **orbitofrontal cortex**, **hippocampus**, **sleep**

- Variables measured: 

- Source paper: *Chung, J. E.; Joo, H. R.; Fan, J. L.; Liu, D. F.; Barnett, A. H.; Chen, S.; Geaghan-Breiner, C.; Karlsson, M. P.; Karlsson, M.; Lee, K. Y.; Liang, H.; Magland, J. F.; Pebbles, J. A.; Tooker, A. C.; Greengard, L. F.; Tolosa, V. M.; Frank, L. M. (2022) Polymer probe recordings from hippocampus (LFP), OFC, NAc, and mPFC*

---

*[DANDI:000066](https://dandiarchive.org/dandiset/000066/draft)*: **Allen Mouse Common Coordinate Framework - Average Brain Template**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **4**, total size (MB): **381.65**

- Variables measured: 

- Source paper: *Ng, Lydia (2022) Allen Mouse Common Coordinate Framework - Average Brain Template*

---

*[DANDI:000067](https://dandiarchive.org/dandiset/000067/draft)*: **Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **28**, total size (MB): **94,565.74**

- Species: **Brown rat**

- Variables measured: **LFP**, **ProcessingModule**, **Units**, **ElectricalSeries**

- Source paper: *Fujisawa, Shigeyoshi; Amarasingham, Asohan; Harrison, Matthew; Buzsáki, György (2022) Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000067_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 5.55 MB | 
[File info](https://api.dandiarchive.org/api/assets/ee7ccc96-3eac-484f-9cc3-2845fee5138b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000067/draft/files?location=sub-EE%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/ee7ccc96-3eac-484f-9cc3-2845fee5138b/download/) 
- NWBE compatibility - file 2: NI  
Size: 5300.47 MB | 
[File info](https://api.dandiarchive.org/api/assets/19691835-bb2e-4aff-ad3e-a7c29407c81e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000067/draft/files?location=sub-GG%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/19691835-bb2e-4aff-ad3e-a7c29407c81e/download/) 
---

*[DANDI:000068](https://dandiarchive.org/dandiset/000068/draft)*: **Testing**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **2**, total size (MB): **0.36**

- Variables measured: **VoltageClampSeries**, **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Testing (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000068_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/8771aac6-7eb9-4cc5-a1cf-2f0ed366e240) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000068/draft/files?location=sub-abcd%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/8771aac6-7eb9-4cc5-a1cf-2f0ed366e240/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000069](https://dandiarchive.org/dandiset/000069/draft)*: **testing_2**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **1**, total size (MB): **297.61**

- Species: **House mouse**

- Variables measured: **CurrentClampSeries**, **PatchClampSeries**, **BehavioralTimeSeries**

- Source paper: *testing_2 (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000069_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 297.61 MB | 
[File info](https://api.dandiarchive.org/api/assets/45aead0c-5666-4c1e-b9b3-83ca00dcd883) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000069/draft/files?location=sub-anm106211%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/45aead0c-5666-4c1e-b9b3-83ca00dcd883/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000070](https://dandiarchive.org/dandiset/000070/draft)*: **Neural population dynamics during reaching**

- Data type: **Neurodata Without Borders (NWB)**, file count: **9**, total size (MB): **45,909.71**

- Species: **Rhesus monkey**

- Variables measured: **Position**, **Units**

- Source paper: *Churchland, Mark; Cunningham, John P.; Kaufman, Matthew T.; Foster, Justin D.; Nuyujukian, Paul; Ryu, Stephen I.; Shenoy, Krishna V. (2022) Neural population dynamics during reaching*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000071](https://dandiarchive.org/dandiset/000071/draft)*: **Brandon's Test Dandiset**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Brandon's Test Dandiset (2022).*

---

*[DANDI:000072](https://dandiarchive.org/dandiset/000072/draft)*: **neural data**

, file count: **0**, total size (MB): **0.0**

- Source paper: *neural data (2022).*

---

*[DANDI:000105](https://dandiarchive.org/dandiset/000105/draft)*: **MGH19-1-021520**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **2**, total size (MB): **2,542,027.98**

- Variables measured: 

- Source paper: *Chung, Kwanghun; Kamentsky, Lee (2022) MGH19-1-021520*

---

*[DANDI:000106](https://dandiarchive.org/dandiset/000106/draft)*: **Electrophysiology data from simultaneous recordings**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Electrophysiology data from simultaneous recordings (2022).*

---

*[DANDI:000107](https://dandiarchive.org/dandiset/000107/draft)*: **IVSCC stimulus sets**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.4**), file count: **1**, total size (MB): **39.29**

- Keywords: **electrophysiology**, **MIES **

- Variables measured: 

- Source paper: *IVSCC stimulus sets (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000107_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 39.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/d2107928-cf16-43a3-a547-691ae3419de9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000107/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d2107928-cf16-43a3-a547-691ae3419de9/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000108](https://dandiarchive.org/dandiset/000108/draft)*: **MITU01 - Light sheet imaging of the human brain**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Kamentsky, Lee (2022) MITU01 - Light sheet imaging of the human brain*

---

*[DANDI:000109](https://dandiarchive.org/dandiset/000109/draft)*: **Patch-seq recordings from human cortex (June 2021)**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **350**, total size (MB): **14,212.58**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortex**

- Variables measured: **ProcessingModule**

- Source paper: *Allen Institute for Brian Science (2022) Patch-seq recordings from human cortex (June 2021)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000109_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 12.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/4a6344f7-e557-41e6-aec2-93e7fff8bd15) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000109/draft/files?location=sub-720619787%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/4a6344f7-e557-41e6-aec2-93e7fff8bd15/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 12.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/07e51937-1cb0-41b1-9b3c-af4d277ad9c7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000109/draft/files?location=sub-651940947%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/07e51937-1cb0-41b1-9b3c-af4d277ad9c7/download/) 
---

*[DANDI:000110](https://dandiarchive.org/dandiset/000110/draft)*: **Foobar**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Foobar (2022).*

---

*[DANDI:000111](https://dandiarchive.org/dandiset/000111/draft)*: **ZZZ**

, file count: **0**, total size (MB): **0.0**

- Source paper: *ZZZ (2022).*

---

*[DANDI:000112](https://dandiarchive.org/dandiset/000112/draft)*: **Test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test (2022).*

---

*[DANDI:000113](https://dandiarchive.org/dandiset/000113/draft)*: **bla**

, file count: **0**, total size (MB): **0.0**

- Source paper: *bla (2022).*

---

*[DANDI:000114](https://dandiarchive.org/dandiset/000114/draft)*: **Single-unit recordings in mouse PVN**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Single-unit recordings in mouse PVN (2022).*

---

*[DANDI:000115](https://dandiarchive.org/dandiset/000115/draft)*: **Gillespie et al (2021) Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice**

- Data type: **Neurodata Without Borders (NWB)**, file count: **57**, total size (MB): **9,103,698.76**

- Species: **Rat; norway rat; rats; brown rat**

- Variables measured: **ElectricalSeries**, **Position**, **SpatialSeries**, **BehavioralEvents**, **ProcessingModule**

- Source paper: *Gillespie, Anna; Astudillo Maya, Daniela; Denovellis, Eric; Liu, Daniel; Kastner, David; Coulter, Michael; Roumis, Demetris; Frank, Loren (2022) Gillespie et al (2021) Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000116](https://dandiarchive.org/dandiset/000116/draft)*: **Test_upload_LiZhang_SpinalCord**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, Guang-Wei (2022) Test_upload_LiZhang_SpinalCord*

---

*[DANDI:000117](https://dandiarchive.org/dandiset/000117/draft)*: **1U01MH116990-01_July_2021**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **197**, total size (MB): **142.55**

- Keywords: **spinal cord**, **patch-clamp**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Zhang, Guang-Wei (2022) 1U01MH116990-01_July_2021*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000117_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/feaa8040-8f0b-47fb-abc2-6d50a434fd13) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000117/draft/files?location=sub-20210511003-2021-05-11-0012%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/feaa8040-8f0b-47fb-abc2-6d50a434fd13/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/29817159-63a3-4da4-986d-ff751ee1b067) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000117/draft/files?location=sub-20210615003-2021-06-15-0018%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/29817159-63a3-4da4-986d-ff751ee1b067/download/) 
---

*[DANDI:000118](https://dandiarchive.org/dandiset/000118/draft)*: **user test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Dichter, Ben (2022) user test*

---

*[DANDI:000119](https://dandiarchive.org/dandiset/000119/draft)*: **ble**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2022) ble*

---

*[DANDI:000120](https://dandiarchive.org/dandiset/000120/draft)*: **test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test*

---

*[DANDI:000121](https://dandiarchive.org/dandiset/000121/draft)*: **Structure and variability of delay activity in premotor cortex**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Even-Chen, Nir; Sheffer, Blue; Vyas, Saurabh; Ryu, Stephen; Shenoy, Krishna (2022) Structure and variability of delay activity in premotor cortex*

---

*[DANDI:000122](https://dandiarchive.org/dandiset/000122/draft)*: **Human fNIRS recordings of motor cortex during finger-tapping task**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **5**, total size (MB): **49.9**

- Keywords: **fNIRS**, **Haemodynamics**, **Motor Cortex**, **Finger Tapping Task**

- Variables measured: 

- Source paper: *Erat Sleiter, Darin (2022) Human fNIRS recordings of motor cortex during finger-tapping task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000122_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 8.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/3af36329-5e0c-4c20-a283-87207b5569f1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000122/draft/files?location=sub-P2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/3af36329-5e0c-4c20-a283-87207b5569f1/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 10.7 MB | 
[File info](https://api.dandiarchive.org/api/assets/911c75ab-51b5-4caa-b930-911b89d2c990) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000122/draft/files?location=sub-P5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/911c75ab-51b5-4caa-b930-911b89d2c990/download/) 
---

*[DANDI:000123](https://dandiarchive.org/dandiset/000123/draft)*: **test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Choudhury, Roni (2022) test*

---

*[DANDI:000124](https://dandiarchive.org/dandiset/000124/draft)*: **footest**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Choudhury, Roni (2022) footest*

---

*[DANDI:000125](https://dandiarchive.org/dandiset/000125/draft)*: **Neural population dynamics during reaching: analysis dataset**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Churchland, Mark; Kauffman, Matthew; Cunningham, John; Foster, Justin; Shenoy, Krishna; Ryu, Stephen; Nuyujukian, Paul (2022) Neural population dynamics during reaching: analysis dataset*

---

*[DANDI:000126](https://dandiarchive.org/dandiset/000126/draft)*: **NWB API Test Data**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **5**, total size (MB): **167.06**

- Species: **House mouse**

- Variables measured: **ProcessingModule**

- Source paper: *Ly, Ryan (2022) NWB API Test Data*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000126_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 36.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/e303dfac-48b1-44de-a847-9cf6154d5ad7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000126/draft/files?location=sub-1001658946%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e303dfac-48b1-44de-a847-9cf6154d5ad7/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000127](https://dandiarchive.org/dandiset/000127/draft)*: **Area2_Bump: macaque somatosensory area 2 spiking activity during reaching with perturbations**

- Data type: **Neurodata Without Borders (NWB)**, file count: **2**, total size (MB): **1,823.37**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **ElectrodeGroup**, **Units**, **SpatialSeries**, **ProcessingModule**

- Source paper: *Chowdhury, Raeed; Miller, Lee (2022) Area2_Bump: macaque somatosensory area 2 spiking activity during reaching with perturbations*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000128](https://dandiarchive.org/dandiset/000128/draft)*: **MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **694.0**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000128_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 690.61 MB | 
[File info](https://api.dandiarchive.org/api/assets/26e85f09-39b7-480f-b337-278a8f034007) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000128/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/26e85f09-39b7-480f-b337-278a8f034007/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000129](https://dandiarchive.org/dandiset/000129/draft)*: **MC_RTT: macaque motor cortex spiking activity during self-paced reaching**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **50.97**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ElectrodeGroup**, **ProcessingModule**

- Source paper: *O'Doherty, Joseph (2022) MC_RTT: macaque motor cortex spiking activity during self-paced reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000129_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 49.76 MB | 
[File info](https://api.dandiarchive.org/api/assets/2ae6bf3c-788b-4ece-8c01-4b4a5680b25b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000129/draft/files?location=sub-Indy%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/2ae6bf3c-788b-4ece-8c01-4b4a5680b25b/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000130](https://dandiarchive.org/dandiset/000130/draft)*: **DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **15.67**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**

- Source paper: *Sohn, Hansem; Jazayeri, Mehrdad (2022) DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000130_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 14.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/c90cbccc-31a5-4815-88e6-822d8c5ca68c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000130/draft/files?location=sub-Haydn%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/c90cbccc-31a5-4815-88e6-822d8c5ca68c/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000131](https://dandiarchive.org/dandiset/000131/draft)*: **Nestdesktop PK**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Nestdesktop PK*

---

*[DANDI:000132](https://dandiarchive.org/dandiset/000132/draft)*: **Neurex Summer School**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Neurex Summer School*

---

*[DANDI:000133](https://dandiarchive.org/dandiset/000133/draft)*: **nest dataset**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) nest dataset*

---

*[DANDI:000134](https://dandiarchive.org/dandiset/000134/draft)*: **neurex**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) neurex*

---

*[DANDI:000135](https://dandiarchive.org/dandiset/000135/draft)*: **Test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Durieux, Laura (2022) Test*

---

*[DANDI:000136](https://dandiarchive.org/dandiset/000136/draft)*: **NEST**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) NEST*

---

*[DANDI:000137](https://dandiarchive.org/dandiset/000137/draft)*: **Neurex Summer School 2021**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Neurex Summer School 2021*

---

*[DANDI:000138](https://dandiarchive.org/dandiset/000138/draft)*: **MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **149.39**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000138_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 148.59 MB | 
[File info](https://api.dandiarchive.org/api/assets/e67b57b2-e9ad-4d95-b9e3-1262997360dc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000138/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e67b57b2-e9ad-4d95-b9e3-1262997360dc/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000139](https://dandiarchive.org/dandiset/000139/draft)*: **MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **77.3**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000139_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 76.6 MB | 
[File info](https://api.dandiarchive.org/api/assets/7ef450a8-8684-42e2-8598-cd38ca2b2e50) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000139/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7ef450a8-8684-42e2-8598-cd38ca2b2e50/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000140](https://dandiarchive.org/dandiset/000140/draft)*: **MC_Maze_Small: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **29.9**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze_Small: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000140_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 29.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/7821971e-c6a4-4568-8773-1bfa205c13f8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000140/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7821971e-c6a4-4568-8773-1bfa205c13f8/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000141](https://dandiarchive.org/dandiset/000141/draft)*: **TravelingDirection_2021**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) TravelingDirection_2021*

---

*[DANDI:000142](https://dandiarchive.org/dandiset/000142/draft)*: **20210923_AIBS_Patchseq_human**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **717**, total size (MB): **26,800.03**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortical**

- Variables measured: **ProcessingModule**

- Source paper: *20210923_AIBS_Patchseq_human (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000142_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 12.72 MB | 
[File info](https://api.dandiarchive.org/api/assets/d4de1978-e106-4ba5-a0bd-ee897cc90b08) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000142/draft/files?location=sub-707724503%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d4de1978-e106-4ba5-a0bd-ee897cc90b08/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 13.49 MB | 
[File info](https://api.dandiarchive.org/api/assets/6646f2ee-2e53-472c-a3a1-52a906ad07ab) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000142/draft/files?location=sub-643277950%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/6646f2ee-2e53-472c-a3a1-52a906ad07ab/download/) 
---

*[DANDI:000143](https://dandiarchive.org/dandiset/000143/draft)*: **IHC Validation Data**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **50**, total size (MB): **10.0**

- Variables measured: 

- Source paper: *DeLorenzo, Lauren (2022) IHC Validation Data*

---

*[DANDI:000144](https://dandiarchive.org/dandiset/000144/draft)*: **croat-test**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **589.06**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**, **TwoPhotonSeries**

- Source paper: *Roat, Chris (2022) croat-test*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000144_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 524.48 MB | 
[File info](https://api.dandiarchive.org/api/assets/bd754a60-c4a8-43fc-b514-87eb4511f29d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000144/draft/files?location=sub-8675309%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/bd754a60-c4a8-43fc-b514-87eb4511f29d/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000145](https://dandiarchive.org/dandiset/000145/draft)*: **Test 2**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Roat, Chris (2022) Test 2*

---

*[DANDI:000146](https://dandiarchive.org/dandiset/000146/draft)*: **NYB**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) NYB*

---

*[DANDI:000147](https://dandiarchive.org/dandiset/000147/draft)*: **PPC_Finger: human posterior parietal cortex recordings during attempted finger movements**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **10**, total size (MB): **77.67**

- Species: **Homo sapiens - Human**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Guan, Charles; Aflalo, Tyson; Zhang, Carey; Andersen, Richard (2022) PPC_Finger: human posterior parietal cortex recordings during attempted finger movements*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000147_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 5.68 MB | 
[File info](https://api.dandiarchive.org/api/assets/d4c985da-5c04-4c39-874b-0c6e22598716) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000147/draft/files?location=sub-P1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d4c985da-5c04-4c39-874b-0c6e22598716/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 6.1 MB | 
[File info](https://api.dandiarchive.org/api/assets/675e49ed-04f2-4281-a4cb-5a1d3363e773) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000147/draft/files?location=sub-P1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/675e49ed-04f2-4281-a4cb-5a1d3363e773/download/) 
---

*[DANDI:000148](https://dandiarchive.org/dandiset/000148/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 01_Oct_2021**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **46**, total size (MB): **929.64**

- Species: **Mus musculus - House mouse**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Zhang, Guang-Wei; Tao, Can; Peng, Bo (2022) Electrophysiological properties of adult mouse spinal cord neurons - 01_Oct_2021*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000148_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 10.26 MB | 
[File info](https://api.dandiarchive.org/api/assets/96cab2be-2416-4fae-8204-618983fe5fcc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000148/draft/files?location=sub-20210728003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/96cab2be-2416-4fae-8204-618983fe5fcc/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 10.42 MB | 
[File info](https://api.dandiarchive.org/api/assets/89f37b43-76e0-45a3-8c88-3ce7f640016c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000148/draft/files?location=sub-20210709003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/89f37b43-76e0-45a3-8c88-3ce7f640016c/download/) 
---

*[DANDI:000149](https://dandiarchive.org/dandiset/000149/draft)*: **IBL ephys data**

- Data type: **Neurodata Without Borders (NWB)**, file count: **4**, total size (MB): **1,980,839.95**

- Species: **House mouse**

- Variables measured: **Position**, **Units**, **BehavioralTimeSeries**, **ElectrodeGroup**

- Source paper: *International Brain Laboratory (2022) IBL ephys data*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000150](https://dandiarchive.org/dandiset/000150/draft)*: **test_release_openscope**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test_release_openscope*

---

*[DANDI:000151](https://dandiarchive.org/dandiset/000151/draft)*: **OpenScope_Credit_assignement_raw_test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Lecoq, Jerome (2022) OpenScope_Credit_assignement_raw_test*

---

*[DANDI:000152](https://dandiarchive.org/dandiset/000152/draft)*: **test_workshop**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2022) test_workshop*

---

*[DANDI:000153](https://dandiarchive.org/dandiset/000153/draft)*: **IEDs**

, file count: **0**, total size (MB): **0.0**

- Source paper: *H Smith, Elliot (2022) IEDs*

---

*[DANDI:000154](https://dandiarchive.org/dandiset/000154/draft)*: **test dandi workshop**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test dandi workshop*

---

*[DANDI:000155](https://dandiarchive.org/dandiset/000155/draft)*: **dandi workshop djd**

, file count: **0**, total size (MB): **0.0**

- Source paper: *denman, daniel (2022) dandi workshop djd*

---

*[DANDI:000156](https://dandiarchive.org/dandiset/000156/draft)*: **dandi workshop to be deleted**

, file count: **0**, total size (MB): **0.0**

- Keywords: **mouse**

- Source paper: *Chrapkiewicz, Radek (2022) dandi workshop to be deleted*

---

*[DANDI:000157](https://dandiarchive.org/dandiset/000157/draft)*: **xiaoai**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) xiaoai*

---

*[DANDI:000158](https://dandiarchive.org/dandiset/000158/draft)*: **My Project**

, file count: **0**, total size (MB): **0.0**

- Source paper: *C. Petersen, Peter (2022) My Project*

---

*[DANDI:000159](https://dandiarchive.org/dandiset/000159/draft)*: **dandi workshop**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) dandi workshop*

---

*[DANDI:000160](https://dandiarchive.org/dandiset/000160/draft)*: **Test_G**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Test_G*

---

*[DANDI:000161](https://dandiarchive.org/dandiset/000161/draft)*: **VD Dandi Workshop Test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) VD Dandi Workshop Test*

---

*[DANDI:000162](https://dandiarchive.org/dandiset/000162/draft)*: **Shin test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Shin test*

---

*[DANDI:000163](https://dandiarchive.org/dandiset/000163/draft)*: **xx**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) xx*

---

*[DANDI:000164](https://dandiarchive.org/dandiset/000164/draft)*: **test**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test*

---

*[DANDI:000165](https://dandiarchive.org/dandiset/000165/draft)*: **Aery Jones et al (2021) Dentate Gyrus and CA3 GABAergic Interneurons Bidirectionally Modulate Signatures of Internal and External Drive to CA1**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **572**, total size (MB): **98,043.54**

- Species: **House mouse**

- Keywords: **hippocampus**, **mouse**, **LFP**

- Variables measured: **Units**, **Position**, **LFP**, **SpatialSeries**, **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Aery Jones, Emily; Rao, Antara; Zilberter, Misha; Djukic, Biljana; Gillespie, Anna K.; Koutsodendris, Nicole; Nelson, Maxine; Yoon, Seo Yeon; Huang, Ky; Yuan, Heidi; Gill, Theodore M.; Huang, Yadong; Frank, Loren M. (2022) Aery Jones et al (2021) Dentate Gyrus and CA3 GABAergic Interneurons Bidirectionally Modulate Signatures of Internal and External Drive to CA1*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000165_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 47.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/b560b456-3473-42dd-9fe2-e7f3cc506731) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000165/draft/files?location=sub-Parsley%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/b560b456-3473-42dd-9fe2-e7f3cc506731/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 51.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/e3a976f9-505f-477f-8ab8-db901dc606b6) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000165/draft/files?location=sub-Sage%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e3a976f9-505f-477f-8ab8-db901dc606b6/download/) 
---

*[DANDI:000166](https://dandiarchive.org/dandiset/000166/draft)*: **Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse**

- Data type: **Neurodata Without Borders (NWB)**, file count: **19**, total size (MB): **787,191.91**

- Species: **House mouse**

- Keywords: **current source density **, **laminar recordings **, **cortex**, **electrophysiology**

- Variables measured: **ElectrodeGroup**, **Units**, **LFP**

- Source paper: *Senzai, Yuta; Fernandez-Ruiz, Antonio; Buzsáki, György (2022) Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000167](https://dandiarchive.org/dandiset/000167/draft)*: **Odor_Set_1**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **5**, total size (MB): **975.79**

- Species: **House mouse**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**

- Source paper: *PIERRÉ, Andrea (2022) Odor_Set_1*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR, CRITICAL, BEST_PRACTICE_VIOLATION](000167_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 182.13 MB | 
[File info](https://api.dandiarchive.org/api/assets/7e5bbff7-c978-4437-b8bf-ec69aa4650b1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000167/draft/files?location=sub-7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7e5bbff7-c978-4437-b8bf-ec69aa4650b1/download/) 
- NWBE compatibility - file 2: NC-1  
Size: 192.94 MB | 
[File info](https://api.dandiarchive.org/api/assets/72ad05cf-8410-40f4-ba0a-0ba86ec298b7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000167/draft/files?location=sub-164%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/72ad05cf-8410-40f4-ba0a-0ba86ec298b7/download/) 
---

*[DANDI:000168](https://dandiarchive.org/dandiset/000168/draft)*: **Simultaneous loose seal cell-attached recordings  and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **170**, total size (MB): **1,379,111.6**

- Species: **Mus musculus - House mouse**

- Keywords: **2-photon**, **visual cortex**, **calcium**, **spike**, **action potential**, **layer 2**, **AAV**, **adeno-associated virus**, **jGCaMP8s**, **jGCaMP8m**, **jGCaMP8f**, **jGCaMP7f**, **XCaMP-Gf**

- Variables measured: **PlaneSegmentation**, **CurrentClampStimulusSeries**, **CurrentClampSeries**, **TwoPhotonSeries**, **ProcessingModule**, **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Rozsa, Marton; Liang, Yajie; Zhang, Yan; Hasseman, Jeremy; Kolb, Ilya; Looger, Loren; Svoboda, Karel; HHMI (2022) Simultaneous loose seal cell-attached recordings  and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR, BEST_PRACTICE_VIOLATION](000168_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 1430.99 MB | 
[File info](https://api.dandiarchive.org/api/assets/026e2006-8779-4d04-83db-7590b47c1afa) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000168/draft/files?location=XCaMPgf%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/026e2006-8779-4d04-83db-7590b47c1afa/download/) 
- NWBE compatibility - file 2: NI  
Size: 1709.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/c442f0bf-49e1-46b8-b9c8-e9d1d7cdcc35) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000168/draft/files?location=jGCaMP8f%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/c442f0bf-49e1-46b8-b9c8-e9d1d7cdcc35/download/) 
---

*[DANDI:000169](https://dandiarchive.org/dandiset/000169/draft)*: **Milti-probe Neuropixels recordings in mouse visual system (additional data)**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Milti-probe Neuropixels recordings in mouse visual system (additional data)*

---

*[DANDI:000170](https://dandiarchive.org/dandiset/000170/draft)*: **CRACK**

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) CRACK*

---

*[DANDI:000171](https://dandiarchive.org/dandiset/000171/draft)*: **Test 1**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Yu, Kai (2022) Test 1*

---

*[DANDI:000172](https://dandiarchive.org/dandiset/000172/draft)*: **UHN whole-cell excitability recordings from mouse cortical neurons**

, file count: **0**, total size (MB): **0.0**

- Keywords: **excitability**, **cortex**, **mouse**

- Source paper: *Howard, Derek; Chameh, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell excitability recordings from mouse cortical neurons*

---

*[DANDI:000173](https://dandiarchive.org/dandiset/000173/draft)*: **Neural Spiking Data in Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **118**, total size (MB): **240.96**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **Ultrasound**, **Plasticity**, **Rat**, **tFUS**, **Somatosensory Cortex**

- Variables measured: **Units**

- Source paper: *Ramachandran, Sandhya; Carnegie Mellon University; Niu, Xiaodan; Yu, Kai; He, Bin (2022) Neural Spiking Data in Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000173_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/748b0311-ec11-49ef-a9c2-e7b1afef72dc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000173/draft/files?location=sub-BH279%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/748b0311-ec11-49ef-a9c2-e7b1afef72dc/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 0.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/cebb65cf-e933-470d-87b4-6660eac86b3e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000173/draft/files?location=sub-BH269%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/cebb65cf-e933-470d-87b4-6660eac86b3e/download/) 
---

*[DANDI:000206](https://dandiarchive.org/dandiset/000206/draft)*: **Visual cortical activity in mice performing naturalistic virtual foraging task**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1**, total size (MB): **118.36**

- Species: **House mouse**

- Variables measured: **SpatialSeries**, **ImagingPlane**, **Position**, **OpticalChannel**

- Source paper: *Smith, Spencer; McGreal, Ryan; Canzano, Joseph (2022) Visual cortical activity in mice performing naturalistic virtual foraging task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000206_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 118.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/e0e142bc-cf1e-4a38-8d24-b54111c404db) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000206/draft/files?location=sub-TIGRE296%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e0e142bc-cf1e-4a38-8d24-b54111c404db/download/) 
- NWBE compatibility - file 2: NI  
---

*[DANDI:000207](https://dandiarchive.org/dandiset/000207/draft)*: **Data for: Neurons detect cognitive boundaries to structure episodic memories in humans (Zheng et al., 2022, Nat Neuro in press)**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **19**, total size (MB): **50.34**

- Species: **Homo sapiens - Human**

- Keywords: **human single neuron**, **hippocampus**, **episodic memory**, **event segmentation**, **amygdala**, **parahippocampal gyrus**, **cognitive boundaries**, **continuous experience**, **ROH consortium**

- Variables measured: **Units**

- Source paper: *Zheng, Jie; Schjetnan, Andrea; Yebra, Mar; Gomes, Bernard; Mosher, Clayton; Kalia, Suneil; Valiante, Taufik; Mamelak, Adam; Kreiman, Gabriel; Rutishauser, Ueli (2022) Data for: Neurons detect cognitive boundaries to structure episodic memories in humans (Zheng et al., 2022, Nat Neuro in press)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000207_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 1.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/aac749db-1b80-4ac8-b1dd-478b881dc24d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000207/draft/files?location=sub-6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/aac749db-1b80-4ac8-b1dd-478b881dc24d/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 1.46 MB | 
[File info](https://api.dandiarchive.org/api/assets/ab57504e-a612-4999-ab11-76fab2393a3d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000207/draft/files?location=sub-10%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/ab57504e-a612-4999-ab11-76fab2393a3d/download/) 
---

*[DANDI:000208](https://dandiarchive.org/dandiset/000208/draft)*: **UHN_mouse_L5_patchclamp**

, file count: **0**, total size (MB): **0.0**

- Source paper: *, Derek (2022) UHN_mouse_L5_patchclamp*

---

*[DANDI:000209](https://dandiarchive.org/dandiset/000209/draft)*: **20211223_AIBS_Patchseq_human**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **291**, total size (MB): **11,109.21**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortical**

- Variables measured: **ProcessingModule**

- Source paper: *Wakeman, Wayne; Kalmbach, Brian; Lein, Ed; Chartrand, Thomas (2022) 20211223_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000209_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 16.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/88d5525f-8f79-4373-8b28-801c89ed5a24) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000209/draft/files?location=sub-731978186%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/88d5525f-8f79-4373-8b28-801c89ed5a24/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 19.03 MB | 
[File info](https://api.dandiarchive.org/api/assets/cd8a87bb-5358-4591-a0b7-8de88573e132) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000209/draft/files?location=sub-1032184063%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/cd8a87bb-5358-4591-a0b7-8de88573e132/download/) 
---

*[DANDI:000210](https://dandiarchive.org/dandiset/000210/draft)*: **Visual cortical activity in mice performing naturalistic virtual foraging task**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Canzano, Joe (2022) Visual cortical activity in mice performing naturalistic virtual foraging task*

---

*[DANDI:000211](https://dandiarchive.org/dandiset/000211/draft)*: **UHN whole-cell excitability recordings from human cortical neurons**

, file count: **0**, total size (MB): **0.0**

- Keywords: **excitability**, **human**, **cortex**

- Source paper: *Howard, Derek; Chameh, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell excitability recordings from human cortical neurons*

---

*[DANDI:000212](https://dandiarchive.org/dandiset/000212/draft)*: **Tracking of Drosophila during egg-laying decisions**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1013**, total size (MB): **9,004.4**

- Species: **Drosophila melanogaster - Fruit fly**

- Keywords: **Drosophila**, **egg laying**, **flies**, **decision making**, **internal expectation**

- Variables measured: **Position**, **ProcessingModule**, **SpatialSeries**

- Source paper: *Vijayan, Vikram; Maimon, Gaby;  National Institutes of Health (2022) Tracking of Drosophila during egg-laying decisions*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000212_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 7.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/b53cc570-a02b-41c8-bce2-7351816b76b2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000212/draft/files?location=sub-0-200-Dop1R2-mutant-2-fly#-21%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/b53cc570-a02b-41c8-bce2-7351816b76b2/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 7.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/8a916887-b90e-4de4-9895-e2bed5adaf1b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000212/draft/files?location=sub-0-200-Dop1R2-mutant-2-fly#-20%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/8a916887-b90e-4de4-9895-e2bed5adaf1b/download/) 
---

*[DANDI:000213](https://dandiarchive.org/dandiset/000213/draft)*: **Transformation of a Spatial Map across the Hippocampal-Lateral Septal Circuit**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **67**, total size (MB): **1,527,009.27**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **hippocampus**, **lateral septum**, **electrophysiology**

- Variables measured: **Position**, **CompassDirection**, **ElectricalSeries**, **LFP**, **Units**, **SpatialSeries**

- Source paper: *Tingley, David; Buzsáki, Gyórgy (2022) Transformation of a Spatial Map across the Hippocampal-Lateral Septal Circuit*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000213_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 746.95 MB | 
[File info](https://api.dandiarchive.org/api/assets/d09a9733-41d8-4696-86bb-e041668247b6) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000213/draft/files?location=sub-DT7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d09a9733-41d8-4696-86bb-e041668247b6/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 826.17 MB | 
[File info](https://api.dandiarchive.org/api/assets/1d183c70-082d-4ce8-b017-05620cc9254f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000213/draft/files?location=sub-DT5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/1d183c70-082d-4ce8-b017-05620cc9254f/download/) 
---

*[DANDI:000214](https://dandiarchive.org/dandiset/000214/draft)*: **Jan_2022_DANDI**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, Guang-Wei (2022) Jan_2022_DANDI*

---

*[DANDI:000215](https://dandiarchive.org/dandiset/000215/draft)*: **1U01MH116990-01_Jan_2022**

, file count: **0**, total size (MB): **0.0**

- Keywords: **spinal cord **

- Source paper: *Zhang, Guang-Wei (2022) 1U01MH116990-01_Jan_2022*

---

*[DANDI:000216](https://dandiarchive.org/dandiset/000216/draft)*: **1U01MH116990-01_Jan_2022**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, Guang-Wei (2022) 1U01MH116990-01_Jan_2022*

---

*[DANDI:000217](https://dandiarchive.org/dandiset/000217/draft)*: **Sniff-synchronized, gradient-guided olfactory search by freely moving mice -- Behavioral Dataset**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1121**, total size (MB): **2,152.04**

- Species: **Mus musculus - House mouse**

- Variables measured: 

- Source paper: *Findley, Teresa; Wyrick, David G; Cramer, Jennifer L; Brown, Morgan A; Holcomb, Blake; Attey, Robin; Yeh, Dorian; Monasevitch, Eric; Nouboussi, Nelly; Cullen, Isabelle; Songco, Jeremea O; King, Jared F; Ahmadian, Yashar; Smear, Matt (2022) Sniff-synchronized, gradient-guided olfactory search by freely moving mice -- Behavioral Dataset*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000217_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/32be659d-80fa-4021-8d6e-4b8cb7e21c2c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000217/draft/files?location=sub-Mouse 2071%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/32be659d-80fa-4021-8d6e-4b8cb7e21c2c/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/d3e786a8-787c-4a80-9dd6-ffeca84a8577) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000217/draft/files?location=sub-Mouse 2083%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d3e786a8-787c-4a80-9dd6-ffeca84a8577/download/) 
---

*[DANDI:000218](https://dandiarchive.org/dandiset/000218/draft)*: **Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **98**, total size (MB): **1,512,863.48**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **hippocampus**, **lateral septum**, **electrophyisology**

- Variables measured: **LFP**, **Units**, **ProcessingModule**, **Position**, **CompassDirection**, **ElectricalSeries**, **SpatialSeries**

- Source paper: *Tingley, David; Buzáki, Gyórgy (2022) Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000218_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 570.69 MB | 
[File info](https://api.dandiarchive.org/api/assets/a6cf3b13-1220-415c-93ad-05d0eeff0f46) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000218/draft/files?location=sub-DT7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a6cf3b13-1220-415c-93ad-05d0eeff0f46/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 638.46 MB | 
[File info](https://api.dandiarchive.org/api/assets/5eb882bd-9242-47bd-bcd0-da548afe01d1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000218/draft/files?location=sub-DT5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/5eb882bd-9242-47bd-bcd0-da548afe01d1/download/) 
---

*[DANDI:000219](https://dandiarchive.org/dandiset/000219/draft)*: **Two photon calcium imaging in the CA1 region of the hippocampus in neonatal mice.**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **62**, total size (MB): **73,147.04**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralEpochs**, **PlaneSegmentation**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Dard, Robin (2022) Two photon calcium imaging in the CA1 region of the hippocampus in neonatal mice*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000219_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 813.61 MB | 
[File info](https://api.dandiarchive.org/api/assets/30aee0ab-a751-4646-9e13-6032be28a0df) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000219/draft/files?location=sub-210226-210308-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/30aee0ab-a751-4646-9e13-6032be28a0df/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 814.67 MB | 
[File info](https://api.dandiarchive.org/api/assets/113a60b6-bfde-4c63-b4cf-10a7821b48c5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000219/draft/files?location=sub-210226-210307-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/113a60b6-bfde-4c63-b4cf-10a7821b48c5/download/) 
---

*[DANDI:000220](https://dandiarchive.org/dandiset/000220/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 25_Jan_2022**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **34**, total size (MB): **1,202.85**

- Species: **Mus musculus - House mouse**

- Variables measured: 

- Source paper: *Zhang, Guang-Wei; Tao, Can; Peng, Bo (2022) Electrophysiological properties of adult mouse spinal cord neurons - 25_Jan_2022*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000220_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 12.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/55463159-6466-48ac-9a7d-c05e2624ef3f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000220/draft/files?location=sub-20190117002%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/55463159-6466-48ac-9a7d-c05e2624ef3f/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 12.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/161cdf76-8cd7-45ce-9551-6a0d15870edf) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000220/draft/files?location=sub-20190315001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/161cdf76-8cd7-45ce-9551-6a0d15870edf/download/) 
---

*[DANDI:000221](https://dandiarchive.org/dandiset/000221/draft)*: **A midbrain-thalamus-cortex circuit reorganizes cortical dynamics to initiate movement**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **263**, total size (MB): **4,422.55**

- Species: **Mus musculus - House mouse**

- Keywords: **Midbrain**, **ALM**, **motor planning**, **movement initiation**

- Variables measured: **SpikeEventSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Inagaki, Hidehiko; Chen, Susu; Svoboda, Karel (2022) A midbrain-thalamus-cortex circuit reorganizes cortical dynamics to initiate movement*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000221_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.41 MB | 
[File info](https://api.dandiarchive.org/api/assets/f02ab674-44f5-4c87-8679-04fa049c7674) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000221/draft/files?location=sub-HI204%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/f02ab674-44f5-4c87-8679-04fa049c7674/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 0.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/de094939-990a-4d6e-af29-dde24936420c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000221/draft/files?location=sub-SC020%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/de094939-990a-4d6e-af29-dde24936420c/download/) 
---

*[DANDI:000222](https://dandiarchive.org/dandiset/000222/draft)*: **O'Hare et al 2022**

, file count: **0**, total size (MB): **0.0**

- Keywords: **neuroscience, dendrites, hippocampus, mouse, plasticity, endoplasmic reticulum, calcium**

- Source paper: *O'Hare, Justin (2022) O'Hare et al 2022*

---

*[DANDI:000223](https://dandiarchive.org/dandiset/000223/draft)*: **Inferring monosynaptic connections from paired spine calcium imaging and large-scale recording of extracellular spiking**

- Data type: **Neurodata Without Borders (NWB)**, file count: **20**, total size (MB): **84,273.72**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **calcium imaging; extracellular recordings; HD-MEA; spike sorting; dendritic spines**

- Variables measured: **PlaneSegmentation**, **ElectrodeGroup**, **ProcessingModule**, **ElectricalSeries**, **TwoPhotonSeries**, **Units**

- Source paper: *Xue, Xiaohan; Buccino, Alessio; Kumar, Sreedhar Saseendran; Hierlemann, Andreas; Bartram, Julian (2022) Inferring monosynaptic connections from paired spine calcium imaging and large-scale recording of extracellular spiking*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000225](https://dandiarchive.org/dandiset/000225/draft)*: **Neural and behavioral**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Khoury, Christine (2022) Neural and behavioral*

---

*[DANDI:000226](https://dandiarchive.org/dandiset/000226/draft)*: **Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **60**, total size (MB): **13,745.15**

- Species: **Mus musculus - House mouse**

- Variables measured: **Units**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Severson, Kyle; Xu, Duo; Van de Loo, Margaret; Bai, Ling; Ginty, David D; OConnor, Daniel H (2022) Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000226_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 19.48 MB | 
[File info](https://api.dandiarchive.org/api/assets/9c90c18a-8e66-4644-a402-e5f849fc08a1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000226/draft/files?location=sub-KSt91%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/9c90c18a-8e66-4644-a402-e5f849fc08a1/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 19.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/0cfad5c5-e44b-424d-bffc-da64ac30fe12) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000226/draft/files?location=sub-KSt119%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/0cfad5c5-e44b-424d-bffc-da64ac30fe12/download/) 
---

*[DANDI:000227](https://dandiarchive.org/dandiset/000227/draft)*: **Electrophysiological recordings in protein hunger neurons of Drosophila Melanogaster**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Liu, Qili (2022) Electrophysiological recordings in protein hunger neurons of Drosophila Melanogaster*

---

*[DANDI:000228](https://dandiarchive.org/dandiset/000228/draft)*: **20220330_AIBS_Patchseq_human**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **91**, total size (MB): **5,816.16**

- Species: **Homo sapiens - Human**

- Keywords: **Patch-seq**, **human**, **neocortical**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Chartrand, Thomas; Kalmbach, Brian; Molnar, Gabor; Tamas, Gabor; Lein, Ed (2022) 20220330_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000228_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 35.66 MB | 
[File info](https://api.dandiarchive.org/api/assets/bdc5f608-caa8-4ac0-a70d-b03a1739ba66) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000228/draft/files?location=sub-H18-28-022%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/bdc5f608-caa8-4ac0-a70d-b03a1739ba66/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 43.37 MB | 
[File info](https://api.dandiarchive.org/api/assets/e42540ff-da70-4dfa-aa9e-05b8512e1e20) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000228/draft/files?location=sub-H20-28-022%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e42540ff-da70-4dfa-aa9e-05b8512e1e20/download/) 
---

*[DANDI:000229](https://dandiarchive.org/dandiset/000229/draft)*: **xxx**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Findley, Teresa (2022) xxx*

---

*[DANDI:000230](https://dandiarchive.org/dandiset/000230/draft)*: **Jacobsen 2022**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **9**, total size (MB): **244.97**

- Species: **Mus musculus - House mouse**

- Variables measured: **CompassDirection**, **Units**, **ElectrodeGroup**, **SpatialSeries**, **ElectricalSeries**, **BehavioralTimeSeries**, **ProcessingModule**, **LFP**, **Position**

- Source paper: *Jacobsen, R Irene; Nair, Rajeevkumar R; Obenhaus, Horst A; Donato, Flavio; Slettmoen, Torstein; Moser, May-Britt; Moser, Edvard I (2022) Jacobsen 2022*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000230_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 24.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/a8f7ef2e-c311-44d8-a72b-2d7bc7e5dc09) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000230/draft/files?location=sub-70375%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a8f7ef2e-c311-44d8-a72b-2d7bc7e5dc09/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 25.5 MB | 
[File info](https://api.dandiarchive.org/api/assets/d8e0ccfb-fc0d-4fd2-8b26-be8f187cc2c0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000230/draft/files?location=sub-58313%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d8e0ccfb-fc0d-4fd2-8b26-be8f187cc2c0/download/) 
---

*[DANDI:000231](https://dandiarchive.org/dandiset/000231/draft)*: **A detailed behavioral, videographic, and neural dataset on object recognition in mice**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **4228**, total size (MB): **1,996,516.62**

- Species: **Mus musculus - House mouse**

- Keywords: **mouse behavior**, **whisker system**, **somatosensory cortex**, **barrel cortex**, **object recognition**, **shape discrimination**, **electrophysiology**, **pose tracking**, **population recordings**, **single unit recordings**

- Variables measured: **BehavioralTimeSeries**, **BehavioralEvents**, **ProcessingModule**, **Units**, **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Rodgers, Chris (2022) A detailed behavioral, videographic, and neural dataset on object recognition in mice*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000231_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 378.69 MB | 
[File info](https://api.dandiarchive.org/api/assets/2374f6b9-babe-4fbd-8cca-df4f8b4ec4c0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000231/draft/files?location=sub-KF119%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/2374f6b9-babe-4fbd-8cca-df4f8b4ec4c0/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 382.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/d45acf3d-aaa9-4f70-ae5d-f70cbc411950) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000231/draft/files?location=sub-219CR%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d45acf3d-aaa9-4f70-ae5d-f70cbc411950/download/) 
---

*[DANDI:000232](https://dandiarchive.org/dandiset/000232/draft)*: **Rule-based modulation of  a sensorimotor transformation across cortical areas**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **86**, total size (MB): **36,639.9**

- Species: **Mus musculus - House mouse**

- Variables measured: **LFP**, **Units**, **BehavioralTimeSeries**, **ElectrodeGroup**, **ProcessingModule**, **ElectricalSeries**

- Source paper: *Chang, Yi-Ting; OConnor, Daniel H (2022) Rule-based modulation of  a sensorimotor transformation across cortical areas*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000232_validation.txt) 

- NWBE compatibility - file 1: NC-1  
Size: 280.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/a1bf6c0a-f424-4491-84b6-596852a2fcae) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000232/draft/files?location=sub-JL005%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a1bf6c0a-f424-4491-84b6-596852a2fcae/download/) 
- NWBE compatibility - file 2: NC-1  
Size: 284.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/a4385201-8913-442c-ba03-41150bf4172d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000232/draft/files?location=sub-YT071%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a4385201-8913-442c-ba03-41150bf4172d/download/) 
---

*[DANDI:000233](https://dandiarchive.org/dandiset/000233/draft)*: **A metabolic function of the hippocampal sharp wave-ripple**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **345**, total size (MB): **12,320,920.24**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **glucose**, **ecephys **, **pharmacology**

- Variables measured: **ElectricalSeries**, **ProcessingModule**, **LFP**, **ElectrodeGroup**

- Source paper: *Tingley, David; McClain, Kathryn; Kaya, Ekin; Carpenter, Jordan; Buzsáki, György (2022) A metabolic function of the hippocampal sharp wave-ripple*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000233_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 18.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/7acfe0c2-1fc1-4060-a423-25ebdd0b3a11) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000233/draft/files?location=sub-CGM57%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7acfe0c2-1fc1-4060-a423-25ebdd0b3a11/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 19.76 MB | 
[File info](https://api.dandiarchive.org/api/assets/80ea45a5-c84c-4b18-aa1d-d9f6b4658c35) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000233/draft/files?location=sub-CGM41%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/80ea45a5-c84c-4b18-aa1d-d9f6b4658c35/download/) 
---

*[DANDI:000239](https://dandiarchive.org/dandiset/000239/draft)*: **Cortical processing of flexible and context-dependent sensorimotor sequences**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **754**, total size (MB): **11,769.9**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralTimeSeries**, **Units**, **ProcessingModule**

- Source paper: *Xu, Duo; Chen, Yuxi; Dong, Mingyuan; Delgado, Angel M; Hughes, Natasha C; Zhang, Linghua; OConnor, Daniel H (2022) Cortical processing of flexible and context-dependent sensorimotor sequences*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000239_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 0.25 MB | 
[File info](https://api.dandiarchive.org/api/assets/656d2d9f-01f5-41b7-8703-31a6a0840302) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000239/draft/files?location=sub-MX180602%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/656d2d9f-01f5-41b7-8703-31a6a0840302/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 0.26 MB | 
[File info](https://api.dandiarchive.org/api/assets/05096d27-a83c-427d-b88a-3801bcf9e63a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000239/draft/files?location=sub-MX180804%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/05096d27-a83c-427d-b88a-3801bcf9e63a/download/) 
---

*[DANDI:000241](https://dandiarchive.org/dandiset/000241/draft)*: **ngff testing**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2022) ngff testing*

---

*[DANDI:000243](https://dandiarchive.org/dandiset/000243/draft)*: **MRI of human ex vivo brainstem**

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **5**, total size (MB): **6,079.71**

- Variables measured: 

- Source paper: *Johnson, G Allan; Calabrese, Evan; Ghosh, Satrajit (2022) MRI of human ex vivo brainstem*

---

*[DANDI:000244](https://dandiarchive.org/dandiset/000244/draft)*: **One photon mesoscale calcium imaging of multiple cell types**

- Data type: **Neurodata Without Borders (NWB)**, file count: **33**, total size (MB): **1,068,310.24**

- Species: **Mus musculus - House mouse**

- Variables measured: **ImagingPlane**, **TwoPhotonSeries**, **OpticalChannel**

- Source paper: *O'Connor, Dave (2022) One photon mesoscale calcium imaging of multiple cell types*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000245](https://dandiarchive.org/dandiset/000245/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 22Q1_Ephys_DANDI**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **25**, total size (MB): **408.91**

- Species: **Mus musculus - House mouse**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Zhang, Guang-Wei; Tao, Can (2022) Electrophysiological properties of adult mouse spinal cord neurons - 22Q1_Ephys_DANDI*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000245_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 8.64 MB | 
[File info](https://api.dandiarchive.org/api/assets/2ff065c2-9991-4b46-a4d6-474f602b891e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000245/draft/files?location=sub-20220317004%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/2ff065c2-9991-4b46-a4d6-474f602b891e/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 8.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/a8bec861-62fa-4f23-bd8a-5cdf83f1695b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000245/draft/files?location=sub-20220119003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a8bec861-62fa-4f23-bd8a-5cdf83f1695b/download/) 
---

*[DANDI:000246](https://dandiarchive.org/dandiset/000246/draft)*: **developing CaMPARI3**

- Data type: **Neurodata Without Borders (NWB)**, file count: **2**, total size (MB): **34,485.96**

- Species: **Mus musculus - House mouse**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **ProcessingModule**, **TwoPhotonSeries**, **PlaneSegmentation**

- Source paper: *Icardi, Jacob (2022) developing CaMPARI3*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000249](https://dandiarchive.org/dandiset/000249/draft)*: **Innate and plastic mechanisms for maternal behaviour in auditory cortex**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **777**, total size (MB): **97,968.24**

- Species: **Mus musculus - House mouse**

- Keywords: **oxytocin**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **TwoPhotonSeries**

- Source paper: *Schiavo, Jennifer K.; Valtcheva, Silvana; Bair-Marshall, Chloe J.; Song, Soomin C.; Martin, Kathleen A.; Froemke, Robert C. (2022) Innate and plastic mechanisms for maternal behaviour in auditory cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000249_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 36.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/7f25d292-0365-4e7d-ae7b-68c8c2124615) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000249/draft/files?location=sub-NV106%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/7f25d292-0365-4e7d-ae7b-68c8c2124615/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 38.08 MB | 
[File info](https://api.dandiarchive.org/api/assets/01fdbd6c-abef-4097-988f-270d45db5ffb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000249/draft/files?location=sub-NV33%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/01fdbd6c-abef-4097-988f-270d45db5ffb/download/) 
---

*[DANDI:000251](https://dandiarchive.org/dandiset/000251/draft)*: **A Unified Framework for Dopamine Signals across Timescales**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **513**, total size (MB): **2,175.64**

- Species: **Mus musculus - House mouse**

- Variables measured: **SpatialSeries**, **ProcessingModule**, **Units**

- Source paper: *Kim, HyungGoo; Malik, Athar; Mikhael, John; Bech, Pol; Tsutsui-Kimura, Iku; Sun, Fangmiao; Zhang, Yajun; Li, Yulong; Watabe-Uchida, Mitsuko; Gershman, Samuel; Uchida, Naoshige (2022) A Unified Framework for Dopamine Signals across Timescales*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000251_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 1.05 MB | 
[File info](https://api.dandiarchive.org/api/assets/5e82f637-fcd8-4587-9a4e-59a14263916c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000251/draft/files?location=sub-3021%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/5e82f637-fcd8-4587-9a4e-59a14263916c/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 1.43 MB | 
[File info](https://api.dandiarchive.org/api/assets/fe98f152-a322-457c-83da-1cca7ada8c5f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000251/draft/files?location=sub-3045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/fe98f152-a322-457c-83da-1cca7ada8c5f/download/) 
---

*[DANDI:000252](https://dandiarchive.org/dandiset/000252/draft)*: **PPC_Finger_RL: human posterior parietal cortex recordings during attempted finger movements of right and left hands**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Guan, Charles (2022) PPC_Finger_RL: human posterior parietal cortex recordings during attempted finger movements of right and left hands*

---

*[DANDI:000255](https://dandiarchive.org/dandiset/000255/draft)*: **A unified 3D map of microscopic architecture and MRI of the human brain**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Bazin, Pierre-Louis (2022) A unified 3D map of microscopic architecture and MRI of the human brain*

---

*[DANDI:000288](https://dandiarchive.org/dandiset/000288/draft)*: **20220630_AIBS_Patchseq_human**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **36**, total size (MB): **1,049.74**

- Species: **Homo sapiens - Human**

- Keywords: **Patch-seq**, **human**

- Variables measured: **VoltageClampSeries**, **CurrentClampStimulusSeries**, **ProcessingModule**, **CurrentClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Mei, Nicholas; Chartrand, Thomas; Kalmbach, Brian; Molnar, Gabor; Tamas, Gabor; Lein, Ed (2022) 20220630_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION](000288_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 13.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/6a254dac-8833-4be4-b782-d0048d129b42) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000288/draft/files?location=sub-H18.03.003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/6a254dac-8833-4be4-b782-d0048d129b42/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 19.14 MB | 
[File info](https://api.dandiarchive.org/api/assets/91e632dc-38bb-42fc-89a5-96c7f7d23443) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000288/draft/files?location=sub-H19.03.316%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/91e632dc-38bb-42fc-89a5-96c7f7d23443/download/) 
---

*[DANDI:000290](https://dandiarchive.org/dandiset/000290/draft)*: **Diaz-Torga_Sfig1**

, file count: **0**, total size (MB): **0.0**

- Source paper: *Abeledo Machado, Alejandra (2022) Diaz-Torga_Sfig1*

---

*[DANDI:000292](https://dandiarchive.org/dandiset/000292/draft)*: **UHN whole-cell patch-clamp excitability recordings from mouse cortical neurons**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **11**, total size (MB): **13.76**

- Species: **Mus musculus - House mouse**

- Keywords: **excitability**, **cortex**, **mouse**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**

- Source paper: *Howard, Derek; Chameh, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell patch-clamp excitability recordings from mouse cortical neurons*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000292_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.94 MB | 
[File info](https://api.dandiarchive.org/api/assets/5eba84f6-1459-4833-9de2-102c65734e4e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000292/draft/files?location=sub-18208024%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/5eba84f6-1459-4833-9de2-102c65734e4e/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 1.04 MB | 
[File info](https://api.dandiarchive.org/api/assets/d98b0dcf-4299-4c06-8843-97750a12d53a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000292/draft/files?location=sub-2018-02-08-0001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d98b0dcf-4299-4c06-8843-97750a12d53a/download/) 
---

*[DANDI:000293](https://dandiarchive.org/dandiset/000293/draft)*: **UHN whole-cell patch-clamp excitability recordings from human cortical neurons**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **121**, total size (MB): **234.98**

- Species: **Homo sapiens - Human**

- Keywords: **excitability**, **human**, **cortex**

- Variables measured: **VoltageClampStimulusSeries**, **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Howard, Derek; Moradi, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell patch-clamp excitability recordings from human cortical neurons*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000293_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/497b0b7f-cf8e-48eb-b949-e730720568a3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000293/draft/files?location=sub-1914-2019-11-28-0038%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/497b0b7f-cf8e-48eb-b949-e730720568a3/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 0.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/e3024e2a-fd3e-447e-9caa-94470aeebc4a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000293/draft/files?location=sub-1911-19o10045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/e3024e2a-fd3e-447e-9caa-94470aeebc4a/download/) 
---

*[DANDI:000294](https://dandiarchive.org/dandiset/000294/draft)*: **A multi-modal fitting approach to construct single-neuron models with patch-clamp and high-density microelectrode arrays**

- Data type: **Neurodata Without Borders (NWB)**, file count: **2**, total size (MB): **18,173.61**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **HD-MEA, patch-clamp, multimodal**

- Variables measured: **ElectricalSeries**, **ProcessingModule**, **CurrentClampSeries**, **CurrentClampStimulusSeries**, **ElectrodeGroup**

- Source paper: *Buccino, Alessio Paolo; Damart, Tanguy; Bartram, Julian; Mandge, Darshan; Xue, Xiaohan; Zbili, Mickael; Gänswein, Tobias; Jaquier, Aurelien; Emmenegger, Vishalini; Markram, Henry; Hierlemann, Andreas; Van Geit, Werner (2022) A multi-modal fitting approach to construct single-neuron models with patch-clamp and high-density microelectrode arrays*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

*[DANDI:000295](https://dandiarchive.org/dandiset/000295/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 22Q2_Ephys_DANDI**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **26**, total size (MB): **476.09**

- Species: **Mus musculus - House mouse**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Zhang, Guang-Wei; Tao, Can (2022) Electrophysiological properties of adult mouse spinal cord neurons - 22Q2_Ephys_DANDI*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000295_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 9.15 MB | 
[File info](https://api.dandiarchive.org/api/assets/75fa33f2-c744-41ff-938b-c16bd345e39d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000295/draft/files?location=sub-20220701004%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/75fa33f2-c744-41ff-938b-c16bd345e39d/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 12.35 MB | 
[File info](https://api.dandiarchive.org/api/assets/5e43b224-33ff-4502-9291-d0a8b57579e1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000295/draft/files?location=sub-20220512002%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/5e43b224-33ff-4502-9291-d0a8b57579e1/download/) 
---

*[DANDI:000296](https://dandiarchive.org/dandiset/000296/draft)*: **Drosophila visual neural responses to stochastic stimuli**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1278**, total size (MB): **745,311.36**

- Species: **Drosophila melanogaster - Fruit fly**

- Variables measured: **ImagingPlane**, **OpticalChannel**, **TwoPhotonSeries**

- Source paper: *Gonzalez, Aneysis (2022) Drosophila visual neural responses to stochastic stimuli*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000296_validation.txt) 

- NWBE compatibility - file 1: LL-V  
Size: 160.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/8269630b-c5c9-4f6c-ba46-f69b007b998d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000296/draft/files?location=sub-3204989286909019890%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/8269630b-c5c9-4f6c-ba46-f69b007b998d/download/) 
- NWBE compatibility - file 2: LL-V  
Size: 170.79 MB | 
[File info](https://api.dandiarchive.org/api/assets/a6254199-b24a-4dca-9296-4ad1b2f94528) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000296/draft/files?location=sub-3342064158402930368%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/a6254199-b24a-4dca-9296-4ad1b2f94528/download/) 
---

*[DANDI:000297](https://dandiarchive.org/dandiset/000297/draft)*: **UHN whole-cell patch-clamp excitability recordings from human cortical neurons**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **118**, total size (MB): **231.1**

- Species: **Homo sapiens - Human**

- Keywords: **excitability**, **human**, **cortex**

- Variables measured: **CurrentClampSeries**, **VoltageClampStimulusSeries**, **CurrentClampStimulusSeries**

- Source paper: *Howard, Derek; Homeira Moradi, Chameh; Taufik A Valiante; Shreejoy Tripathy (2022) UHN whole-cell patch-clamp excitability recordings from human cortical neurons*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000297_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/0722fb00-ede2-4dcc-8f5d-005319c92e7e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000297/draft/files?location=sub-1914-2019-11-28-0038%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/0722fb00-ede2-4dcc-8f5d-005319c92e7e/download/) 
- NWBE compatibility - file 2: LL-P  
Size: 0.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/d2763c7d-a040-4c14-9327-fe8aca272a81) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000297/draft/files?location=sub-1911-19o10045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/d2763c7d-a040-4c14-9327-fe8aca272a81/download/) 
---

*[DANDI:000298](https://dandiarchive.org/dandiset/000298/draft)*: **Brain_stim_and_FSCV_and_ensemble_recording_anesthetized**

, file count: **0**, total size (MB): **0.0**

- Keywords: **FSCV, electrophysiology, brain stimulation**

- Source paper: *Cowen, Stephen (2022) Brain_stim_and_FSCV_and_ensemble_recording_anesthetized*

---

*[DANDI:000299](https://dandiarchive.org/dandiset/000299/draft)*: **Stephen Test Set**

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1**, total size (MB): **0.23**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Cowen, Stephen (2022) Stephen Test Set*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000299_validation.txt) 

- NWBE compatibility - file 1: LL-P  
Size: 0.23 MB | 
[File info](https://api.dandiarchive.org/api/assets/12bb96be-3535-4144-82b5-4f23abe76b32) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000299/draft/files?location=sub-Rat203%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/hub/nwbfile=https://api.dandiarchive.org/api/assets/12bb96be-3535-4144-82b5-4f23abe76b32/download/) 
- NWBE compatibility - file 2: NI  
---

</p></details>