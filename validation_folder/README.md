# Summary statistics for available Dandisets
Last updated: 2024-01-25

## BIDS Dandisets

- Total number of BIDS Dandisets: 8

- Median number of files in each BIDS Dandiset: 12.5

- Median number of bytes in each BIDS Dandiset: 1,135,998,101


## NWB Dandisets

- Total number of NWB Dandisets: 216

- Median number of files in each NWB Dandiset: 36.5

- Median number of bytes in each NWB Dandiset: 19,208,737,173

- 6 most commonly measured variables: ProcessingModule, Units, ElectrodeGroup, ElectricalSeries, PlaneSegmentation, BehavioralTimeSeries

- NWB Dandisets that pass NWBInspector and thus are possibly NWBE compatible

[000005](#000005), [000008](#000008), [000010](#000010), [000012](#000012), [000013](#000013), [000015](#000015), [000019](#000019), [000021](#000021), [000027](#000027), [000034](#000034), [000035](#000035), [000037](#000037), [000043](#000043), [000045](#000045), [000048](#000048), [000053](#000053), [000056](#000056), [000059](#000059), [000064](#000064), [000067](#000067), [000068](#000068), [000069](#000069), [000107](#000107), [000114](#000114), [000117](#000117), [000122](#000122), [000126](#000126), [000128](#000128), [000129](#000129), [000130](#000130), [000138](#000138), [000139](#000139), [000140](#000140), [000144](#000144), [000147](#000147), [000148](#000148), [000165](#000165), [000168](#000168), [000173](#000173), [000212](#000212), [000213](#000213), [000217](#000217), [000218](#000218), [000220](#000220), [000221](#000221), [000226](#000226), [000230](#000230), [000232](#000232), [000233](#000233), [000239](#000239), [000245](#000245), [000247](#000247), [000249](#000249), [000250](#000250), [000251](#000251), [000252](#000252), [000292](#000292), [000293](#000293), [000295](#000295), [000296](#000296), [000297](#000297), [000299](#000299), [000301](#000301), [000302](#000302), [000338](#000338), [000339](#000339), [000341](#000341), [000351](#000351), [000363](#000363), [000398](#000398), [000399](#000399), [000404](#000404), [000405](#000405), [000409](#000409), [000411](#000411), [000454](#000454), [000458](#000458), [000462](#000462), [000463](#000463), [000469](#000469), [000470](#000470), [000481](#000481), [000482](#000482), [000488](#000488), [000489](#000489), [000529](#000529), [000535](#000535), [000537](#000537), [000538](#000538), [000544](#000544), [000545](#000545), [000547](#000547), [000548](#000548), [000549](#000549), [000550](#000550), [000552](#000552), [000561](#000561), [000566](#000566), [000572](#000572), [000574](#000574), [000575](#000575), [000579](#000579), [000582](#000582), [000618](#000618), [000623](#000623), [000625](#000625), [000631](#000631), [000633](#000633), [000637](#000637), [000640](#000640), [000673](#000673), [000678](#000678), [000683](#000683), [000728](#000728), [000732](#000732), [000784](#000784)

- NWBE compatibility terminology: 
  - **LL-P**: Likely plottable - file whose datatypes extend TimeSeries that can be viewed and plotted 
  - **LL-V**: Likely viewable - file whose datatypes might not extend TimeSeries that can be viewed 
  - **NC-0**: Not compatible level 0 - file cannot be opened 
  - **NC-1**: Not compatible level 1 - geppetto model for file cannot be created 
  - **NI**: No information - file is not tested 

<details open><summary> Summary information on the available Dandisets (full details in <a href="dandiset_summary.csv">dandiset_summary.csv</a>).
</summary><p>



---
<a id="000003">*[DANDI:000003](https://dandiarchive.org/dandiset/000003/draft)*: **Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **101**, total size (MB): **2,559,248.01**

- Species: **House mouse**

- Keywords: **cell types**, **current source density**, **laminar recordings**, **oscillations**, **mossy cells**, **granule cells**, **optogenetics**

- Variables measured: **DecompositionSeries**, **LFP**, **Units**, **Position**, **ElectricalSeries**

- Source paper: *Senzai, Yuta; Fernandez-Ruiz, Antonio; Buzsáki, György (2023) Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000004">*[DANDI:000004](https://dandiarchive.org/dandiset/000004/draft)*: **A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **87**, total size (MB): **6,197.47**

- Species: **Human**

- Keywords: **cognitive neuroscience**, **data standardization**, **decision making**, **declarative memory**, **neurophysiology**, **neurosurgery**, **NWB**, **open source**, **single-neurons**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Chandravadia, Nand; Liang, Dehua; Schjetnan, Andrea Gomez Palacio; Carlson, April; Faraut, Mailys; Chung, Jeffrey M.; Reed, Chrystal M.; Dichter, Ben; Maoz, Uri; Kalia, Suneil K.; Valiante, Taufik A.; Mamelak, Adam N.; Rutishauser, Ueli (2023) A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, CRITICAL, BEST_PRACTICE_VIOLATION](000004_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 54.65 MB | 
[File info](https://api.dandiarchive.org/api/assets/a831c980-7b5a-4ad2-9687-7caf5ae27c56) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000004/draft/files?location=sub-P16HMH%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a831c980-7b5a-4ad2-9687-7caf5ae27c56/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 54.68 MB | 
[File info](https://api.dandiarchive.org/api/assets/e22c078c-43d9-4713-84f5-02d2e1db707c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000004/draft/files?location=sub-P15HMH%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e22c078c-43d9-4713-84f5-02d2e1db707c/download/) 
---

<a id="000005">*[DANDI:000005](https://dandiarchive.org/dandiset/000005/draft)*: **Electrophysiology data from thalamic and cortical neurons during somatosensation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **148**, total size (MB): **46,436.69**

- Species: **House mouse**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **OptogeneticSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Yu, Jianing; Gutnisky, Diego A; Hires, S Andrew; Svoboda, Karel (2022) Electrophysiology data from thalamic and cortical neurons during somatosensation*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000005_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 46.54 MB | 
[File info](https://api.dandiarchive.org/api/assets/3ee6887c-1462-4d39-a3f3-e0e356e673d5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000005/draft/files?location=sub-anm266945%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3ee6887c-1462-4d39-a3f3-e0e356e673d5/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 58.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/b73da40b-a5bf-4f1c-9cfc-479b1ea4d0f3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000005/draft/files?location=sub-anm266951%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b73da40b-a5bf-4f1c-9cfc-479b1ea4d0f3/download/) 
---

<a id="000006">*[DANDI:000006](https://dandiarchive.org/dandiset/000006/draft)*: **Mouse anterior lateral motor cortex (ALM) in delay response task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0.2**), file count: **53**, total size (MB): **139.6**

- Species: **House mouse**

- Variables measured: **Units**, **ElectrodeGroup**, **BehavioralEvents**

- Source paper: *Economo, Michael N.; Svoboda, Karel (2022) Mouse anterior lateral motor cortex (ALM) in delay response task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000006_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/32cb0ae9-49fd-4bf9-b939-3960df7aeca2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000006/draft/files?location=sub-anm369963%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/32cb0ae9-49fd-4bf9-b939-3960df7aeca2/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 0.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/e949d5c5-ed3d-4e17-9adf-a7facab36870) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000006/draft/files?location=sub-anm372795%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e949d5c5-ed3d-4e17-9adf-a7facab36870/download/) 
---

<a id="000007">*[DANDI:000007](https://dandiarchive.org/dandiset/000007/draft)*: **A cortico-cerebellar loop for motor planning**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **54**, total size (MB): **199.44**

- Species: **House mouse**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Gao, Zhenyu; Davis, Courtney; Thomas, Alyse M.; Economo, Michael N.; Abrego, Amada M.; Svoboda, Karel; Zeeuw, Chris I. De; Li, Nuo (2022) A cortico-cerebellar loop for motor planning*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000007_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.54 MB | 
[File info](https://api.dandiarchive.org/api/assets/558d1353-a52e-4d06-a027-cadbbffaa25c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000007/draft/files?location=sub-anm00314758%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/558d1353-a52e-4d06-a027-cadbbffaa25c/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/c093327c-6a1f-4290-a972-ef9976a48576) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000007/draft/files?location=sub-BAYLORCD13%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c093327c-6a1f-4290-a972-ef9976a48576/download/) 
---

<a id="000008">*[DANDI:000008](https://dandiarchive.org/dandiset/000008/draft)*: **Phenotypic variation within and across transcriptomic cell types in mouse motor cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1328**, total size (MB): **11,922.33**

- Species: **Mus musculus - House mouse**

- Keywords: **Patch-seq**, **cortex**, **motor cortex**, **mouse**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Scala, Federico; Kobak, Dmitry; Bernabucci, Matteo; Bernaerts, Yves; Cadwell, Cathryn Rene; Castro, Jesus Ramon; Hartmanis, Leonard; Jiang, Xiaolong; Laturnus, Sophie; Miranda, Elanine; Mulherkar, Shalaka; Tan, Zheng Huan; Yao, Zizhen; Zeng, Hongkui; Sandberg, Rickard; Berens, Philipp; Tolias, Andreas Savas (2022) Phenotypic variation within and across transcriptomic cell types in mouse motor cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000008_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 3.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/6810513d-2d2e-4ed0-b5b5-f221025d766e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000008/draft/files?location=sub-mouse-KKXUD%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/6810513d-2d2e-4ed0-b5b5-f221025d766e/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 3.25 MB | 
[File info](https://api.dandiarchive.org/api/assets/874c6994-6535-41af-9d20-3a9763fb6df2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000008/draft/files?location=sub-mouse-UALZV%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/874c6994-6535-41af-9d20-3a9763fb6df2/download/) 
---

<a id="000009">*[DANDI:000009](https://dandiarchive.org/dandiset/000009/draft)*: **Maintenance of persistent activity in a frontal thalamocortical loop**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **173**, total size (MB): **12,919.71**

- Species: **House mouse**

- Variables measured: **Units**, **ElectrodeGroup**, **ProcessingModule**, **BehavioralTimeSeries**, **CurrentClampStimulusSeries**, **OptogeneticSeries**

- Source paper: *Guo, Zengcai; Inagaki, Hidehiko; Daie, Kayvon; Druckmann, Shaul; Gerfen, Charles R.; Svoboda, Karel (2022) Maintenance of persistent activity in a frontal thalamocortical loop*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000009_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/8ce1a50f-11bd-4a75-a510-64c3f32bb529) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000009/draft/files?location=sub-anm00264942%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8ce1a50f-11bd-4a75-a510-64c3f32bb529/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/10f60b99-4286-4780-a767-f0267d877abd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000009/draft/files?location=sub-anm00237800%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/10f60b99-4286-4780-a767-f0267d877abd/download/) 
---

<a id="000010">*[DANDI:000010](https://dandiarchive.org/dandiset/000010/draft)*: **A motor cortex circuit for motor planning and movement**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **158**, total size (MB): **40,006.57**

- Species: **House mouse**

- Variables measured: **BehavioralTimeSeries**, **Units**, **ElectrodeGroup**, **BehavioralEvents**, **PlaneSegmentation**

- Source paper: *Li, Nuo; Chen, Tsai-Wen; Guo, Zengcai V.; Gerfen, Charles R.; Svoboda, Karel (2022) A motor cortex circuit for motor planning and movement*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000010_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 26.71 MB | 
[File info](https://api.dandiarchive.org/api/assets/427d4e22-35b3-4775-8d82-f4598ecdcc87) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000010/draft/files?location=sub-217951%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/427d4e22-35b3-4775-8d82-f4598ecdcc87/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 27.77 MB | 
[File info](https://api.dandiarchive.org/api/assets/348c64a2-381a-470b-891d-d5de316b3ad8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000010/draft/files?location=sub-226244%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/348c64a2-381a-470b-891d-d5de316b3ad8/download/) 
---

<a id="000011">*[DANDI:000011](https://dandiarchive.org/dandiset/000011/draft)*: **Robust neuronal dynamics in premotor cortex during motor planning**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **92**, total size (MB): **32,435.33**

- Species: **House mouse**

- Variables measured: **BehavioralEvents**, **ElectrodeGroup**, **Units**, **BehavioralTimeSeries**

- Source paper: *Li, Nuo; Daie, Kayvon; Svoboda, Karel; Druckmann, Shaul (2022) Robust neuronal dynamics in premotor cortex during motor planning*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000011_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 89.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/354d36fd-fa87-4bc4-adaf-ba5b846d38ef) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000011/draft/files?location=sub-291064%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/354d36fd-fa87-4bc4-adaf-ba5b846d38ef/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 164.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/bc019955-f5d3-4fec-ab7a-e01ed12f493b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000011/draft/files?location=sub-291063%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/bc019955-f5d3-4fec-ab7a-e01ed12f493b/download/) 
---

<a id="000012">*[DANDI:000012](https://dandiarchive.org/dandiset/000012/draft)*: **Kriegstein2020**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **297**, total size (MB): **487.52**

- Species: **Human**

- Variables measured: **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Zhou, Li; Kriegstein, Arnold (2022) Kriegstein2020*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000012_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.26 MB | 
[File info](https://api.dandiarchive.org/api/assets/06a78426-1ea5-4a66-b4df-3fb112387dc5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000012/draft/files?location=sub-2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/06a78426-1ea5-4a66-b4df-3fb112387dc5/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 0.47 MB | 
[File info](https://api.dandiarchive.org/api/assets/82eaa51c-c79f-4219-bc06-b0aa330ccbce) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000012/draft/files?location=sub-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/82eaa51c-c79f-4219-bc06-b0aa330ccbce/download/) 
---

<a id="000013">*[DANDI:000013](https://dandiarchive.org/dandiset/000013/draft)*: **Low-noise encoding of active touch by layer 4 in the somatosensory cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **52**, total size (MB): **11,408.74**

- Species: **House mouse**

- Variables measured: **BehavioralTimeSeries**, **CurrentClampSeries**, **PatchClampSeries**

- Source paper: *Hires, Samuel; Gutnisky, Diego; Yu, Jianing; O'Connor, Daniel H; Svoboda, Karel (2022) Low-noise encoding of active touch by layer 4 in the somatosensory cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000013_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 47.98 MB | 
[File info](https://api.dandiarchive.org/api/assets/061d6422-018a-4fe0-b914-119b9297be7d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000013/draft/files?location=sub-anm244024%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/061d6422-018a-4fe0-b914-119b9297be7d/download/) | 
[File Summary](Summaries/000013/file_0/README.md) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 59.92 MB | 
[File info](https://api.dandiarchive.org/api/assets/b8b1b393-e001-452f-b48f-a7b78b09a582) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000013/draft/files?location=sub-anm266945%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b8b1b393-e001-452f-b48f-a7b78b09a582/download/) | 
[File Summary](Summaries/000013/file_1/README.md) 
---

<a id="000015">*[DANDI:000015](https://dandiarchive.org/dandiset/000015/draft)*: **A Map of Anticipatory Activity in Mouse Motor Cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **210**, total size (MB): **17,159.73**

- Species: **House mouse**

- Variables measured: **BehavioralEvents**, **PlaneSegmentation**

- Source paper: *Chen, Tsai-Wen; Li, Nuo; Daie, Kayvon; Svoboda, Karel (2022) A Map of Anticipatory Activity in Mouse Motor Cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000015_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 16.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/70c2d486-4f4b-4821-9f37-540cb1e28de2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000015/draft/files?location=sub-an044%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/70c2d486-4f4b-4821-9f37-540cb1e28de2/download/) | 
[File Summary](Summaries/000015/file_0/README.md) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 30.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/72138f7e-5f52-43f8-be08-8cd608764166) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000015/draft/files?location=sub-an043%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/72138f7e-5f52-43f8-be08-8cd608764166/download/) | 
[File Summary](Summaries/000015/file_1/README.md) 
---

<a id="000016">*[DANDI:000016](https://dandiarchive.org/dandiset/000016/draft)*: **Excitatory and inhibitory subnetworks are equally selective during decision-making and emerge simultaneously during learning**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **135**, total size (MB): **62,572.04**

- Variables measured: **BehavioralTimeSeries**, **PlaneSegmentation**

- Source paper: *Najafi, Farzaneh; Churchland, Anne K. (2022) Excitatory and inhibitory subnetworks are equally selective during decision-making and emerge simultaneously during learning*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000016_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 199.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/913646f8-4d02-45f5-b830-85dfc69ae74a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000016/draft/files?location=sub-mouse2-fni17%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/913646f8-4d02-45f5-b830-85dfc69ae74a/download/) | 
[File Summary](Summaries/000016/file_0/README.md) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 214.5 MB | 
[File info](https://api.dandiarchive.org/api/assets/b24bfa76-2a06-440f-9b3a-8e06de9ce493) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000016/draft/files?location=sub-mouse1-fni16%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b24bfa76-2a06-440f-9b3a-8e06de9ce493/download/) | 
[File Summary](Summaries/000016/file_1/README.md) 
---

<a id="000017">*[DANDI:000017](https://dandiarchive.org/dandiset/000017/draft)*: **Distributed coding of choice, action and engagement across the mouse brain**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **39**, total size (MB): **14,682.59**

- Species: **House mouse**

- Keywords: **neuropixels**

- Variables measured: **ProcessingModule**, **PupilTracking**, **BehavioralEpochs**, **Units**, **BehavioralEvents**, **BehavioralTimeSeries**, **ElectrodeGroup**

- Source paper: *Steinmetz, Nicholas; Zatka-Haas, Peter; Carandini, Matteo; Harris, Kenneth; Wang, Renee (2022) Distributed coding of choice, action and engagement across the mouse brain*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, CRITICAL, BEST_PRACTICE_VIOLATION](000017_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 216.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/3722e6b8-d47f-4feb-a9ae-9c368e41166b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000017/draft/files?location=sub-Lederberg%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3722e6b8-d47f-4feb-a9ae-9c368e41166b/download/) | 
[File Summary](Summaries/000017/file_0/README.md) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 272.08 MB | 
[File info](https://api.dandiarchive.org/api/assets/9a19c19e-c91d-4d3c-ac97-ad98c621634f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000017/draft/files?location=sub-Richards%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/9a19c19e-c91d-4d3c-ac97-ad98c621634f/download/) | 
[File Summary](Summaries/000017/file_1/README.md) 
---

<a id="000018">*[DANDI:000018](https://dandiarchive.org/dandiset/000018/draft)*: **Mouse Spinal Cord Ephys Dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Tao, Can; Zhang, Guang-Wei (2022) Mouse Spinal Cord Ephys Dataset*

---

<a id="000019">*[DANDI:000019](https://dandiarchive.org/dandiset/000019/draft)*: **Human ECoG speaking consonant-vowel syllables**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0.2**), file count: **31**, total size (MB): **55,585.86**

- Species: **Human**

- Keywords: **electrocorticography (ECoG)**, **speech production**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**, **ProcessingModule**, **Spectrum**

- Source paper: *Bouchard, Kristofer E.; Chang, Edward F. (2023) Human ECoG speaking consonant-vowel syllables*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000019_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1099.89 MB | 
[File info](https://api.dandiarchive.org/api/assets/fbd3bc15-d716-495f-814d-1aa14f8d3b45) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000019/draft/files?location=sub-GP31%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/fbd3bc15-d716-495f-814d-1aa14f8d3b45/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 1551.06 MB | 
[File info](https://api.dandiarchive.org/api/assets/911776e7-aebc-4206-b8f3-01f66c7bf747) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000019/draft/files?location=sub-GP33%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/911776e7-aebc-4206-b8f3-01f66c7bf747/download/) 
---

<a id="000020">*[DANDI:000020](https://dandiarchive.org/dandiset/000020/draft)*: **Patch-seq recordings from mouse visual cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **4435**, total size (MB): **141,856.44**

- Species: **House mouse**

- Keywords: **Patch-seq**, **mouse**, **visual cortex**, **interneuron**

- Variables measured: **ProcessingModule**

- Source paper: *Allen Institute for Brain Science (2022) Patch-seq recordings from mouse visual cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000020_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 11.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/17f31e2b-26b4-4c3e-8e98-423769cc3912) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000020/draft/files?location=sub-639391596%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/17f31e2b-26b4-4c3e-8e98-423769cc3912/download/) | 
[File Summary](Summaries/000020/file_0/README.md) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 12.05 MB | 
[File info](https://api.dandiarchive.org/api/assets/df0ed794-e7b5-45a0-9f7f-5aa75e70348d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000020/draft/files?location=sub-643830482%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/df0ed794-e7b5-45a0-9f7f-5aa75e70348d/download/) | 
[File Summary](Summaries/000020/file_1/README.md) 
---

<a id="000021">*[DANDI:000021](https://dandiarchive.org/dandiset/000021/draft)*: **20191003_AIBS_mouse_ecephys_brain_observatory_1_1**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **214**, total size (MB): **477,562.34**

- Species: **House mouse**

- Keywords: **electrophysiology**, **life sciences**, **machine learning**, **neurobiology**, **signal processing**

- Variables measured: **ProcessingModule**, **LFP**, **Units**

- Source paper: *Siegle, Josh; Wakeman, Wayne; Jia, Xiaoxuan; Heller, Gregg; Ramirez, Tamina; Graddis, Nile; Mei, Nicholas; Durand, Severine (2022) 20191003_AIBS_mouse_ecephys_brain_observatory_1_1*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000021_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 72.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/4d5f1bda-3d20-46f0-a0c8-20f3a3ee9d54) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000021/draft/files?location=sub-703279277%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4d5f1bda-3d20-46f0-a0c8-20f3a3ee9d54/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 898.78 MB | 
[File info](https://api.dandiarchive.org/api/assets/e1f0127e-f5d7-4cac-a42c-bb76127f2ddc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000021/draft/files?location=sub-719828686%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e1f0127e-f5d7-4cac-a42c-bb76127f2ddc/download/) 
---

<a id="000022">*[DANDI:000022](https://dandiarchive.org/dandiset/000022/draft)*: **20191003_AIBS_mouse_ecephys_functional_connectivity**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **169**, total size (MB): **374,956.84**

- Species: **House mouse**

- Keywords: **electrophysiology**, **life sciences**, **machine learning**, **neurobiology**, **signal processing**

- Variables measured: **LFP**, **ProcessingModule**, **Units**

- Source paper: *Siegle, Josh; Wakeman, Wayne; Jia, Xiaoxuan; Durand, Severine; Heller, Gregg; Ramirez, Tamina; Graddis, Nile; Mei, Nicholas (2022) 20191003_AIBS_mouse_ecephys_functional_connectivity*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000023">*[DANDI:000023](https://dandiarchive.org/dandiset/000023/draft)*: **Patch-seq recordings from human cortex (June 2020)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **318**, total size (MB): **12,401.58**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortex**, ** layer 2/3**

- Variables measured: **ProcessingModule**

- Source paper: *Allen Institute for Brian Science (2022) Patch-seq recordings from human cortex (June 2020)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000023_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 13.5 MB | 
[File info](https://api.dandiarchive.org/api/assets/7687363f-dd32-4325-9f40-705227fd470c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000023/draft/files?location=sub-695464588%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7687363f-dd32-4325-9f40-705227fd470c/download/) | 
[File Summary](Summaries/000023/file_0/README.md) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 14.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/20991256-4a71-48bb-ae0a-e4ccaf29a192) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000023/draft/files?location=sub-731978186%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/20991256-4a71-48bb-ae0a-e4ccaf29a192/download/) | 
[File Summary](Summaries/000023/file_1/README.md) 
---

<a id="000024">*[DANDI:000024](https://dandiarchive.org/dandiset/000024/draft)*: **LFP & MUA from BF**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **LFP, BF, interhemispheric**

- Source paper: *LFP & MUA from BF (2022).*

---

<a id="000025">*[DANDI:000025](https://dandiarchive.org/dandiset/000025/draft)*: **Example intracellular ephys data from LNMC & BBP**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1**, total size (MB): **13.66**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **VoltageClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Example intracellular ephys data from LNMC & BBP (2022).*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: UNABLE

---

<a id="000026">*[DANDI:000026](https://dandiarchive.org/dandiset/000026/draft)*: **Human brain cell census for BA 44/45**</a>

, file count: **1**, total size (MB): **0.0**

- Keywords: **multi-modal imaging**, **MRI**, **OCT**, **SPIM**, **human cortex**, **Broca's area**, **Motor cortex**, **Stereology**

- Source paper: *Mazzamuto, Giacomo; Costantini, Irene; Gavryusev, Vladislav; Castelli, Filippo Maria; Pesce, Luca; Scardigli, Marina; Pavone, Francesco Saverio; Roffilli, Matteo; Silvestri, Ludovico; Brady, Niamh; Ramazzotti, Josephine; Hof, Patrick R.; Boas, David A.; Fischl, Bruce; Morgan, Leah; Yang, Jiarui; Chang, Shuaibin; Laffey, Jessie; Magnain, Caroline; Varadarajan, Divya; Wang, Hui; Frost, Robert; Kouwe, Andre van der; Player, Allison Stevens; Atzeni, Alessia; Gonzalez, Juan Eugenio Iglesias; Balbastre, Yael; Vera, Matthew; Cordero, Devani; Nestor, Kimberly; Ammon, William; Nolan, Jackson; Mora, Jocelyn; Pallares, Erendira Garcia; Augustinack, Jean; Diamond, Bram; Fogarty, Morgan; Boyd, Emma; Varghese, Merina; Dalca, Adrian V.; Edlow, Brian; Frosche, Matthew; Wicinski, Bridget; Chen, I-Chun Anderson (2023) Human brain cell census for BA 44/45*

---

<a id="000027">*[DANDI:000027](https://dandiarchive.org/dandiset/000027/draft)*: **Test dataset for testing dandi-cli.**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0b**), file count: **1**, total size (MB): **0.02**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **development**

- Variables measured: 

- Source paper: *Halchenko, Yaroslav O. (2023) Test dataset for testing dandi-cli*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000027_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.02 MB | 
[File info](https://api.dandiarchive.org/api/assets/838bab7b-9ab4-4d66-97b3-898a367c9c7e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000027/draft/files?location=sub-RAT123%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/838bab7b-9ab4-4d66-97b3-898a367c9c7e/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000028">*[DANDI:000028](https://dandiarchive.org/dandiset/000028/draft)*: **Simulated cortical Neuropixels recording with ground truth**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **3**, total size (MB): **42,942.23**

- Species: **House mouse**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**, **Units**

- Source paper: *Simulated cortical Neuropixels recording with ground truth (2022).*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000029">*[DANDI:000029](https://dandiarchive.org/dandiset/000029/draft)*: **Test dataset for development purposes**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.0.2**), file count: **9**, total size (MB): **39.01**

- Species: **Macaca mulatta - Rhesus monkey**

- Keywords: **development**

- Variables measured: **ProcessingModule**, **ElectrodeGroup**, **BehavioralEvents**, **Units**

- Source paper: *Last, First; Test Org (2023) Test dataset for development purposes*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000029_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.02 MB | 
[File info](https://api.dandiarchive.org/api/assets/356b20b7-ae80-4d42-9715-075492eb025d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000029/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/356b20b7-ae80-4d42-9715-075492eb025d/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 6.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/669355cb-a494-4106-a394-347d424fddf8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000029/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/669355cb-a494-4106-a394-347d424fddf8/download/) 
---

<a id="000030">*[DANDI:000030](https://dandiarchive.org/dandiset/000030/draft)*: **Allen Brain Observatory Neuropixels recording**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Allen Brain Observatory Neuropixels recording (2022).*

---

<a id="000031">*[DANDI:000031](https://dandiarchive.org/dandiset/000031/draft)*: **ABC**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *ABC (2022).*

---

<a id="000032">*[DANDI:000032](https://dandiarchive.org/dandiset/000032/draft)*: **Test dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Dichter, Benjamin (2023) Test dataset*

---

<a id="000033">*[DANDI:000033](https://dandiarchive.org/dandiset/000033/draft)*: **Test-2 dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test-2 dataset (2022).*

---

<a id="000034">*[DANDI:000034](https://dandiarchive.org/dandiset/000034/draft)*: **SpikeInterface, a unified framework for spike sorting**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **6**, total size (MB): **74,351.01**

- Species: **House mouse**

- Keywords: **Spike Sorting**, **extracellular electrophysiology**

- Variables measured: **ElectrodeGroup**, **Units**, **ElectricalSeries**

- Source paper: *Buccino, Alessio; Hurwitz, Cole; Garcia, Samuel; Magland, Jeremy; Siegle, Joshua; Hurwitz, Roger; Hennig, Matthias H. (2022) SpikeInterface, a unified framework for spike sorting*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000034_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 11.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/c696fc2b-d2e6-4e27-8775-01657193c4a2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000034/draft/files?location=sub-mouse412804%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c696fc2b-d2e6-4e27-8775-01657193c4a2/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 6470.91 MB | 
[File info](https://api.dandiarchive.org/api/assets/9822a813-0dec-4d07-810b-1c13341c168d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000034/draft/files?location=sub-P29-16-05-14-retina02-left%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/9822a813-0dec-4d07-810b-1c13341c168d/download/) 
---

<a id="000035">*[DANDI:000035](https://dandiarchive.org/dandiset/000035/draft)*: **Temperature-controlled intracellular Patch-seq recordings in mouse motor cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.1.0**), file count: **185**, total size (MB): **1,656.17**

- Species: **House mouse**

- Keywords: **Patch-seq**, **mouse**, **cortex**, **motor cortex**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Scala, Federico; Kobak, Dmitry; Bernabucci, Matteo; Bernaerts, Yves; Cadwell, Cathryn Rene; Castro, Jesus Ramon; Hartmanis, Leonard; Jiang, Xiaolong; Laturnus, Sophie; Miranda, Elanine; Mulherkar, Shalaka; Tan, Zheng Huan; Yao, Zizhen; Last, First; Zeng, Hongkui; Sandberg, Rickard; Berens, Philipp; Tolias, Andreas Savas (2022) Temperature-controlled intracellular Patch-seq recordings in mouse motor cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000035_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 4.63 MB | 
[File info](https://api.dandiarchive.org/api/assets/f1fe5b46-ca4d-4884-83e1-25e3b008bdb2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000035/draft/files?location=sub-mouse-WPOGH%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f1fe5b46-ca4d-4884-83e1-25e3b008bdb2/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 5.69 MB | 
[File info](https://api.dandiarchive.org/api/assets/d3f3b662-45ee-4c14-88b5-2c96caa28b9a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000035/draft/files?location=sub-mouse-MITSU%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d3f3b662-45ee-4c14-88b5-2c96caa28b9a/download/) 
---

<a id="000036">*[DANDI:000036](https://dandiarchive.org/dandiset/000036/draft)*: **Allen Institute Openscope - Measuring Stimulus-Evoked Neurophysiological Differentiation in Distinct Populations of Neurons in Mouse Visual Cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **57**, total size (MB): **79,771.34**

- Keywords: **two photon imaging**, **visual stimuli**, **mice**, **openscope**

- Variables measured: **BehavioralTimeSeries**, **PlaneSegmentation**

- Source paper: *Lecoq, Jerome; Mayner, Will (2023) Allen Institute Openscope - Measuring Stimulus-Evoked Neurophysiological Differentiation in Distinct Populations of Neurons in Mouse Visual Cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000036_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 1306.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/3ff75d8e-318f-47d1-805a-1b409b1600e2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000036/draft/files?location=sub-406876%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3ff75d8e-318f-47d1-805a-1b409b1600e2/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 1310.77 MB | 
[File info](https://api.dandiarchive.org/api/assets/3988673a-e876-4a0e-83c3-12dc35229a7f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000036/draft/files?location=sub-389014%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3988673a-e876-4a0e-83c3-12dc35229a7f/download/) 
---

<a id="000037">*[DANDI:000037](https://dandiarchive.org/dandiset/000037/draft)*: **Allen Institute Openscope - Responses to inconsistent stimuli in somata and distal apical dendrites in primary visual cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **150**, total size (MB): **2,484,974.04**

- Species: **Mus musculus - House mouse**

- Keywords: **learning**, **neocortex**, **pyramidal neurons**, **distal apical dendrites**, **somata**, **L2/3**, **L5**, **two-photon calcium imaging**, **mouse VisP**, **prediction**, **credit assignment**

- Variables measured: **ProcessingModule**, **SpatialSeries**, **PlaneSegmentation**, **OpticalChannel**, **BehavioralTimeSeries**, **ImagingPlane**, **PupilTracking**, **TwoPhotonSeries**

- Source paper: *Gillon, Colleen J.; Lecoq, Jérôme A.; Pina, Jason E.; Zylberberg, Joel; Richards, Blake A. (2023) Allen Institute Openscope - Responses to inconsistent stimuli in somata and distal apical dendrites in primary visual cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000037_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 150.7 MB | 
[File info](https://api.dandiarchive.org/api/assets/af450eea-0023-445e-9ea2-3dc5bd5538fd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000037/draft/files?location=sub-418779%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/af450eea-0023-445e-9ea2-3dc5bd5538fd/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 206.84 MB | 
[File info](https://api.dandiarchive.org/api/assets/3749be7d-96cf-4cd5-afc7-11a4882943ec) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000037/draft/files?location=sub-411771%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3749be7d-96cf-4cd5-afc7-11a4882943ec/download/) 
---

<a id="000038">*[DANDI:000038](https://dandiarchive.org/dandiset/000038/draft)*: **Testytest**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Testytest (2022).*

---

<a id="000039">*[DANDI:000039](https://dandiarchive.org/dandiset/000039/draft)*: **Allen Institute – Contrast tuning in mouse visual cortex with calcium imaging**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **100**, total size (MB): **22,607.25**

- Species: **House mouse**

- Keywords: **vision**, **visual cortex**, **inhibition**, **inhibitory circuits**, **circuit dynamics**, **gain control**

- Variables measured: **Units**, **PlaneSegmentation**, **TwoPhotonSeries**, **BehavioralTimeSeries**

- Source paper: *Millman, Dan; Vries, Saskia de (2023) Allen Institute – Contrast tuning in mouse visual cortex with calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000039_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 31.31 MB | 
[File info](https://api.dandiarchive.org/api/assets/645adfe1-7fdf-48f0-9c61-304df785e92d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000039/draft/files?location=sub-664605504%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/645adfe1-7fdf-48f0-9c61-304df785e92d/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 31.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/7b8def8d-69aa-44e3-be02-057c8f1864f0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000039/draft/files?location=sub-678530120%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7b8def8d-69aa-44e3-be02-057c8f1864f0/download/) 
---

<a id="000040">*[DANDI:000040](https://dandiarchive.org/dandiset/000040/draft)*: **Neuropixels recordings in mouse visual system**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **Neuropixels**

- Source paper: *Jia, Xiaoxuan; Siegle, Josh; Durand, Severine; Heller, Gregg; Ramirez, Tamina (2022) Neuropixels recordings in mouse visual system*

---

<a id="000041">*[DANDI:000041](https://dandiarchive.org/dandiset/000041/draft)*: **Network Homeostasis and State Dynamics of Neocortical Sleep**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **22**, total size (MB): **154,863.46**

- Species: **Brown rat**

- Keywords: **Firing patterns**, **Sleep/awake states**, **Sleep stages**, **Homeostasis**

- Variables measured: **Units**, **LFP**, **ElectricalSeries**

- Source paper: *Watson, Brendon O.; Levenstein, Daniel; Greene, J. Palmer; Gelinas, Jennifer N.; Buzsáki, György (2022) Network Homeostasis and State Dynamics of Neocortical Sleep*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000042">*[DANDI:000042](https://dandiarchive.org/dandiset/000042/draft)*: **Allen Institute Openscope - Meaningful project  - Full movies**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Allen Institute Openscope - Meaningful project  - Full movies (2022).*

---

<a id="000043">*[DANDI:000043](https://dandiarchive.org/dandiset/000043/draft)*: **Human, macaque, and mouse L5 pyramidal neuron physiology**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.4**), file count: **94**, total size (MB): **3,271.28**

- Species: **House mouse**

- Keywords: **Patch-seq**, **Motor cortex**, **Betz cell**, **Human**, **Macaque**, **Mouse**

- Variables measured: 

- Source paper: *Kalmbach, Brian; Ting, Jonathan; Owen, Scott; Lein, Ed (2022) Human, macaque, and mouse L5 pyramidal neuron physiology*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000043_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 14.76 MB | 
[File info](https://api.dandiarchive.org/api/assets/26f67672-5162-4f43-86cb-402aed8c582d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000043/draft/files?location=sub-M19-01-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/26f67672-5162-4f43-86cb-402aed8c582d/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 16.17 MB | 
[File info](https://api.dandiarchive.org/api/assets/d715f810-df3f-42b4-8650-e0c64a236ac1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000043/draft/files?location=sub-Q19-26-018%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d715f810-df3f-42b4-8650-e0c64a236ac1/download/) 
---

<a id="000044">*[DANDI:000044](https://dandiarchive.org/dandiset/000044/draft)*: **Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **8**, total size (MB): **65,708.92**

- Species: **Brown rat**

- Variables measured: **ElectricalSeries**, **LFP**, **Units**

- Source paper: *Grosmark, Andres D.; Buzsáki, György (2022) Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000045">*[DANDI:000045](https://dandiarchive.org/dandiset/000045/draft)*: **IBL behavioral data**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **6615**, total size (MB): **97,844.92**

- Species: **House mouse**

- Keywords: **International Brain Laboratory**

- Variables measured: **BehavioralTimeSeries**, **ProcessingModule**, **Position**, **DecompositionSeries**, **ElectrodeGroup**

- Source paper: *International Brain Laboratory (2022) IBL behavioral data*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000045_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/7946c765-52e4-44e2-90ae-9652f8a956e2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000045/draft/files?location=sub-354e6122-de4a-4945-bafd-d46df65768f6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7946c765-52e4-44e2-90ae-9652f8a956e2/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.32 MB | 
[File info](https://api.dandiarchive.org/api/assets/3d982a78-0f0d-4313-a9ed-60a9bdf42db9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000045/draft/files?location=sub-00778394-c956-408d-8a6c-ca3b05a611d5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3d982a78-0f0d-4313-a9ed-60a9bdf42db9/download/) 
---

<a id="000046">*[DANDI:000046](https://dandiarchive.org/dandiset/000046/draft)*: **asdf**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *asdf (2022).*

---

<a id="000047">*[DANDI:000047](https://dandiarchive.org/dandiset/000047/draft)*: **Test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test (2022).*

---

<a id="000048">*[DANDI:000048](https://dandiarchive.org/dandiset/000048/draft)*: **Electrical and optical physiology in in vivo population-scale two-photon calcium imaging**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1**, total size (MB): **590.27**

- Variables measured: **PlaneSegmentation**, **TwoPhotonSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Ledochowitsch, Peter; Huang, Lawrence; Knoblich, Ulf; Oliver, Michael; Lecoq, Jerome; Reid, Clay; Li, Lu; Zeng, Hongkui; Koch, Christof; Waters, Jack; Vries, Saskia E.J. de; Buice, Michael A. (2023) Electrical and optical physiology in in vivo population-scale two-photon calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000048_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 590.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/827b4c2f-4235-4350-b40f-02e120211dcd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000048/draft/files?location=sub-222549%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/827b4c2f-4235-4350-b40f-02e120211dcd/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000049">*[DANDI:000049](https://dandiarchive.org/dandiset/000049/draft)*: **Allen Institute – TF x SF tuning in mouse visual cortex with calcium imaging**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **78**, total size (MB): **22,211.89**

- Species: **House mouse**

- Keywords: **Mouse**, **2-photon calcium imaging**, **visual cortex**

- Variables measured: **TwoPhotonSeries**, **Units**, **PlaneSegmentation**, **BehavioralTimeSeries**

- Source paper: *Millman, Daniel; de Vries, Saskia (2023) Allen Institute – TF x SF tuning in mouse visual cortex with calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000049_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 33.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/38cf16f0-0f4c-44ec-b04e-0b0c0b02781b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000049/draft/files?location=sub-760940732%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/38cf16f0-0f4c-44ec-b04e-0b0c0b02781b/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 50.59 MB | 
[File info](https://api.dandiarchive.org/api/assets/7f81af9c-fab1-4a4a-9ca6-992bbbb0a4b3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000049/draft/files?location=sub-759066288%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7f81af9c-fab1-4a4a-9ca6-992bbbb0a4b3/download/) 
---

<a id="000050">*[DANDI:000050](https://dandiarchive.org/dandiset/000050/draft)*: **Allen Institute - Run Tuning in the Mouse Visual Cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **56**, total size (MB): **26,372.58**

- Species: **House mouse**

- Variables measured: **TwoPhotonSeries**, **Units**, **PlaneSegmentation**, **BehavioralTimeSeries**

- Source paper: *Allen Institute - Run Tuning in the Mouse Visual Cortex (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000050_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 94.81 MB | 
[File info](https://api.dandiarchive.org/api/assets/f3de94e9-6af4-4169-b911-1e7028ca2021) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000050/draft/files?location=sub-673580710%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f3de94e9-6af4-4169-b911-1e7028ca2021/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 155.38 MB | 
[File info](https://api.dandiarchive.org/api/assets/55583159-e897-4b77-8a81-48c78e8b6227) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000050/draft/files?location=sub-753847689%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/55583159-e897-4b77-8a81-48c78e8b6227/download/) 
---

<a id="000051">*[DANDI:000051](https://dandiarchive.org/dandiset/000051/draft)*: **pons8-yo_16xdownsampled**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1**, total size (MB): **585.93**

- Species: **Human**

- Variables measured: 

- Source paper: *pons8-yo_16xdownsampled (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000051_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 585.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/203fdd15-60d6-41c4-b964-3439163e4e3a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000051/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/203fdd15-60d6-41c4-b964-3439163e4e3a/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000052">*[DANDI:000052](https://dandiarchive.org/dandiset/000052/draft)*: **Pons8-BIDS-16xdownsampled**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **518**, total size (MB): **226.8**

- Variables measured: 

- Source paper: *Pons8-BIDS-16xdownsampled (2022).*

---

<a id="000053">*[DANDI:000053](https://dandiarchive.org/dandiset/000053/draft)*: **Recordings from medial entorhinal cortex during linear track and open exploration**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **359**, total size (MB): **1,393,128.77**

- Species: **House mouse**

- Keywords: **neuropixel**, **entorhinal cortex**

- Variables measured: **LFP**, **Position**, **Units**, **ElectrodeGroup**, **EyeTracking**, **SpatialSeries**, **ProcessingModule**

- Source paper: *Mallory, Caitlin S.; Hardcastle, Kiah; Campbell, Malcolm G.; Attinger, Alexander; Low, Isabel I. C.; Raymond, Jennifer L.; Giocomo, Lisa M. (2022) Recordings from medial entorhinal cortex during linear track and open exploration*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000053_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 2.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/cefaf356-0f24-4ebb-8970-3ca91d97b405) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000053/draft/files?location=sub-Ella%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/cefaf356-0f24-4ebb-8970-3ca91d97b405/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 2.48 MB | 
[File info](https://api.dandiarchive.org/api/assets/fcce9de1-149d-4ab3-b3a8-9803239fa70a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000053/draft/files?location=sub-Barbara%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/fcce9de1-149d-4ab3-b3a8-9803239fa70a/download/) 
---

<a id="000054">*[DANDI:000054](https://dandiarchive.org/dandiset/000054/draft)*: **Plitt & Giocomo (2021) Experience Dependent Contextual Codes in the Hippocampus. Nat Neuro**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **85**, total size (MB): **1,959,122.44**

- Species: **House mouse**

- Variables measured: **PlaneSegmentation**, **TwoPhotonSeries**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Plitt, Mark; Giocomo, Lisa M. (2022) Plitt & Giocomo (2021) Experience Dependent Contextual Codes in the Hippocampus. Nat Neuro*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000055">*[DANDI:000055](https://dandiarchive.org/dandiset/000055/draft)*: **AJILE12: Long-term naturalistic human intracranial neural recordings and pose**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **55**, total size (MB): **845,869.7**

- Species: **Human**

- Variables measured: **Position**, **ProcessingModule**, **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Peterson, Steven M.; Singh, Satpreet H.; Dichter, Benjamin; Scheid, Micheal; Rao, Rajesh P. N.; Brunton, Bingni W. (2022) AJILE12: Long-term naturalistic human intracranial neural recordings and pose*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000056">*[DANDI:000056](https://dandiarchive.org/dandiset/000056/draft)*: **Internally organized mechanisms of the head direction sense**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **40**, total size (MB): **207,733.01**

- Species: **House mouse**

- Keywords: ****

- Variables measured: **ElectricalSeries**, **Units**, **LFP**, **Position**, **ProcessingModule**

- Source paper: *Peyrache, Adrien; Lacroix, Marie M; Petersen, Peter C; Buzsáki, György (2022) Internally organized mechanisms of the head direction sense*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000056_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 1306.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/ada02790-6eb6-48ee-902d-9ba017303586) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000056/draft/files?location=sub-Mouse24%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ada02790-6eb6-48ee-902d-9ba017303586/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 1892.07 MB | 
[File info](https://api.dandiarchive.org/api/assets/748aa5de-c0de-4aa7-a7ef-2aad2f87a7eb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000056/draft/files?location=sub-Mouse20%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/748aa5de-c0de-4aa7-a7ef-2aad2f87a7eb/download/) 
---

<a id="000057">*[DANDI:000057](https://dandiarchive.org/dandiset/000057/draft)*: **foobar**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *foobar (2022).*

---

<a id="000058">*[DANDI:000058](https://dandiarchive.org/dandiset/000058/draft)*: **MITU01 Dataset**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **17**, total size (MB): **35,328.36**

- Variables measured: 

- Source paper: *MITU01 Dataset (2022).*

---

<a id="000059">*[DANDI:000059](https://dandiarchive.org/dandiset/000059/draft)*: **Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **98**, total size (MB): **2,934,037.57**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ProcessingModule**, **Position**, **ElectrodeGroup**, **SpatialSeries**, **Units**, **LFP**, **ElectricalSeries**

- Source paper: *Petersen, Peter; Buzsáki, György (2023) Cooling of Medial Septum Reveals Theta Phase Lag Coordination of Hippocampal Cell Assemblies*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000059_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 3.52 MB | 
[File info](https://api.dandiarchive.org/api/assets/cb30bd19-f8e8-40f8-aaab-21d45ba76c63) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000059/draft/files?location=sub-MS10%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/cb30bd19-f8e8-40f8-aaab-21d45ba76c63/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 10.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/4800ef4e-6161-4612-be95-9371ee6d2daf) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000059/draft/files?location=sub-MS22%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4800ef4e-6161-4612-be95-9371ee6d2daf/download/) 
---

<a id="000060">*[DANDI:000060](https://dandiarchive.org/dandiset/000060/draft)*: **Dataset for Finkelstein, Fontolan et al. "Attractor dynamics gate cortical information flow during decision-making"**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **98**, total size (MB): **1,009.09**

- Species: **House mouse**

- Keywords: **motor cortex**, **extracellular electrophysiology**, **decision-making**, **attractor**, **optogenetic stimulation**

- Variables measured: **Units**, **BehavioralEvents**

- Source paper: *Finkelstein, Arseny; Svoboda, Karel (2022) Dataset for Finkelstein, Fontolan et al. "Attractor dynamics gate cortical information flow during decision-making"*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000060_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/1ecaa50a-5751-46ae-9fef-5e381472b108) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000060/draft/files?location=sub-353938%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1ecaa50a-5751-46ae-9fef-5e381472b108/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 1.98 MB | 
[File info](https://api.dandiarchive.org/api/assets/f2dd0e64-2c91-4ef6-92b8-84dd3141119e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000060/draft/files?location=sub-365942%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f2dd0e64-2c91-4ef6-92b8-84dd3141119e/download/) 
---

<a id="000061">*[DANDI:000061](https://dandiarchive.org/dandiset/000061/draft)*: **Reactivations of emotional memory in the hippocampus–amygdala system during sleep**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **40**, total size (MB): **1,952,634.65**

- Species: **Brown rat**

- Variables measured: **Units**, **LFP**, **ElectricalSeries**, **ProcessingModule**

- Source paper: *Girardeau, Gabrielle; Inema, Ingrid; Buzsáki, György (2022) Reactivations of emotional memory in the hippocampus–amygdala system during sleep*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000063">*[DANDI:000063](https://dandiarchive.org/dandiset/000063/draft)*: **UHN_human_heterogeneity**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *UHN_human_heterogeneity (2022).*

---

<a id="000064">*[DANDI:000064](https://dandiarchive.org/dandiset/000064/draft)*: **Simulation extension example**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **1**, total size (MB): **218.37**

- Variables measured: 

- Source paper: *Raikov, Ivan; Milstein, Aaron; Soltesz, Ivan (2022) Simulation extension example*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000064_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 218.37 MB | 
[File info](https://api.dandiarchive.org/api/assets/bb61e86d-e28f-4da7-b07a-44dfa377cf32) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000064/draft/files?location=sub-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/bb61e86d-e28f-4da7-b07a-44dfa377cf32/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000065">*[DANDI:000065](https://dandiarchive.org/dandiset/000065/draft)*: **Polymer probe recordings from hippocampus (LFP), OFC, NAc, and mPFC**</a>

, file count: **1**, total size (MB): **237,685.09**

- Keywords: **rat, **, **polymer probe**, **electrophysiology**, **nucleus accumbens**, **medial prefrontal cortex**, **orbitofrontal cortex**, **hippocampus**, **sleep**

- Variables measured: 

- Source paper: *Chung, J. E.; Joo, H. R.; Fan, J. L.; Liu, D. F.; Barnett, A. H.; Chen, S.; Geaghan-Breiner, C.; Karlsson, M. P.; Karlsson, M.; Lee, K. Y.; Liang, H.; Magland, J. F.; Pebbles, J. A.; Tooker, A. C.; Greengard, L. F.; Tolosa, V. M.; Frank, L. M. (2022) Polymer probe recordings from hippocampus (LFP), OFC, NAc, and mPFC*

---

<a id="000066">*[DANDI:000066](https://dandiarchive.org/dandiset/000066/draft)*: **Allen Mouse Common Coordinate Framework - Average Brain Template**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **4**, total size (MB): **381.65**

- Variables measured: 

- Source paper: *Ng, Lydia (2023) Allen Mouse Common Coordinate Framework - Average Brain Template*

---

<a id="000067">*[DANDI:000067](https://dandiarchive.org/dandiset/000067/draft)*: **Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **28**, total size (MB): **94,565.74**

- Species: **Brown rat**

- Variables measured: **LFP**, **ProcessingModule**, **Units**, **ElectricalSeries**

- Source paper: *Fujisawa, Shigeyoshi; Amarasingham, Asohan; Harrison, Matthew; Buzsáki, György (2022) Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000067_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 5.55 MB | 
[File info](https://api.dandiarchive.org/api/assets/ee7ccc96-3eac-484f-9cc3-2845fee5138b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000067/draft/files?location=sub-EE%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ee7ccc96-3eac-484f-9cc3-2845fee5138b/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 5300.47 MB | 
[File info](https://api.dandiarchive.org/api/assets/19691835-bb2e-4aff-ad3e-a7c29407c81e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000067/draft/files?location=sub-GG%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/19691835-bb2e-4aff-ad3e-a7c29407c81e/download/) 
---

<a id="000068">*[DANDI:000068](https://dandiarchive.org/dandiset/000068/draft)*: **Testing**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **2**, total size (MB): **0.36**

- Variables measured: **VoltageClampSeries**, **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Testing (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000068_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/8771aac6-7eb9-4cc5-a1cf-2f0ed366e240) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000068/draft/files?location=sub-abcd%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8771aac6-7eb9-4cc5-a1cf-2f0ed366e240/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000069">*[DANDI:000069](https://dandiarchive.org/dandiset/000069/draft)*: **testing_2**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.2**), file count: **1**, total size (MB): **297.61**

- Species: **House mouse**

- Variables measured: **CurrentClampSeries**, **PatchClampSeries**, **BehavioralTimeSeries**

- Source paper: *testing_2 (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000069_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 297.61 MB | 
[File info](https://api.dandiarchive.org/api/assets/45aead0c-5666-4c1e-b9b3-83ca00dcd883) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000069/draft/files?location=sub-anm106211%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/45aead0c-5666-4c1e-b9b3-83ca00dcd883/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000070">*[DANDI:000070](https://dandiarchive.org/dandiset/000070/draft)*: **Neural population dynamics during reaching**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **9**, total size (MB): **45,909.71**

- Species: **Rhesus monkey**

- Variables measured: **Position**, **Units**

- Source paper: *Churchland, Mark; Cunningham, John P.; Kaufman, Matthew T.; Foster, Justin D.; Nuyujukian, Paul; Ryu, Stephen I.; Shenoy, Krishna V. (2022) Neural population dynamics during reaching*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000071">*[DANDI:000071](https://dandiarchive.org/dandiset/000071/draft)*: **Brandon's Test Dandiset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Brandon's Test Dandiset (2022).*

---

<a id="000072">*[DANDI:000072](https://dandiarchive.org/dandiset/000072/draft)*: **neural data**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *neural data (2022).*

---

<a id="000105">*[DANDI:000105](https://dandiarchive.org/dandiset/000105/draft)*: **MGH19-1-021520**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **2**, total size (MB): **2,542,027.98**

- Variables measured: 

- Source paper: *Chung, Kwanghun; Kamentsky, Lee (2022) MGH19-1-021520*

---

<a id="000106">*[DANDI:000106](https://dandiarchive.org/dandiset/000106/draft)*: **Electrophysiology data from simultaneous recordings**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Electrophysiology data from simultaneous recordings (2022).*

---

<a id="000107">*[DANDI:000107](https://dandiarchive.org/dandiset/000107/draft)*: **IVSCC stimulus sets**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.4**), file count: **1**, total size (MB): **39.29**

- Keywords: **electrophysiology**, **MIES **

- Variables measured: 

- Source paper: *IVSCC stimulus sets (2022).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000107_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 39.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/d2107928-cf16-43a3-a547-691ae3419de9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000107/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d2107928-cf16-43a3-a547-691ae3419de9/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000108">*[DANDI:000108](https://dandiarchive.org/dandiset/000108/draft)*: **Light sheet imaging of the human brain**</a>

, file count: **1**, total size (MB): **0.0**

- Source paper: *Kamentsky, Lee; Marx, Slayton; Park, Juhyuk; Su-Arcaro, Clover; Moukheiber, Mira; Zhao, Victor (2023) Light sheet imaging of the human brain*

---

<a id="000109">*[DANDI:000109](https://dandiarchive.org/dandiset/000109/draft)*: **Patch-seq recordings from human cortex (June 2021)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **350**, total size (MB): **14,212.58**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortex**

- Variables measured: **ProcessingModule**

- Source paper: *Allen Institute for Brian Science (2022) Patch-seq recordings from human cortex (June 2021)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000109_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 12.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/4a6344f7-e557-41e6-aec2-93e7fff8bd15) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000109/draft/files?location=sub-720619787%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4a6344f7-e557-41e6-aec2-93e7fff8bd15/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 12.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/07e51937-1cb0-41b1-9b3c-af4d277ad9c7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000109/draft/files?location=sub-651940947%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/07e51937-1cb0-41b1-9b3c-af4d277ad9c7/download/) 
---

<a id="000110">*[DANDI:000110](https://dandiarchive.org/dandiset/000110/draft)*: **Foobar**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Foobar (2022).*

---

<a id="000111">*[DANDI:000111](https://dandiarchive.org/dandiset/000111/draft)*: **ZZZ**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *ZZZ (2023).*

---

<a id="000112">*[DANDI:000112](https://dandiarchive.org/dandiset/000112/draft)*: **Test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Test (2022).*

---

<a id="000113">*[DANDI:000113](https://dandiarchive.org/dandiset/000113/draft)*: **bla**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *bla (2022).*

---

<a id="000114">*[DANDI:000114](https://dandiarchive.org/dandiset/000114/draft)*: **Oxytocin neurons enable social transmission of maternal behaviour**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **28**, total size (MB): **306,892.2**

- Species: **Mus musculus - House mouse**

- Keywords: **oxytocin**, **alloparenting**, **maternal behavior**

- Variables measured: **ProcessingModule**, **ElectrodeGroup**, **ElectricalSeries**, **Units**

- Source paper: *Carcea, Ioana; Caraballo, Naomi López; Marlin, Bianca J.; Ooyama, Rumi; Riceberg, Justin S.; Mendoza Navarro, Joyce M.; Opendak, Maya; Diaz, Veronica E.; Schuster, Luisa; Alvarado Torres, Maria I.; Lethin, Harper; Ramos, Daniel; Minder, Jessica; Mendoza, Sebastian L.; Bair-Marshall, Chloe J.; Samadjopoulos, Grace H.; Hidema, Shizu; Falkner, Annegret; Lin, Dayu; Mar, Adam; Wadghiri, Youssef Z.; Nishimori, Katsuhiko; Kikusui, Takefumi; Mogi, Kazutaka; Sullivan, Regina M.; Froemke, Robert C. (2023) Oxytocin neurons enable social transmission of maternal behaviour*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000114_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 12.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/6d3e01db-4f0a-440c-b411-39e7bfb10d96) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000114/draft/files?location=sub-ROV49%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/6d3e01db-4f0a-440c-b411-39e7bfb10d96/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 13.64 MB | 
[File info](https://api.dandiarchive.org/api/assets/1a1e6b88-5392-453b-9645-c18d30acb876) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000114/draft/files?location=sub-ROV43%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1a1e6b88-5392-453b-9645-c18d30acb876/download/) 
---

<a id="000115">*[DANDI:000115](https://dandiarchive.org/dandiset/000115/draft)*: **Gillespie et al (2021) Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **57**, total size (MB): **9,103,698.76**

- Species: **Rat; norway rat; rats; brown rat**

- Variables measured: **ElectricalSeries**, **Position**, **SpatialSeries**, **BehavioralEvents**, **ProcessingModule**

- Source paper: *Gillespie, Anna; Astudillo Maya, Daniela; Denovellis, Eric; Liu, Daniel; Kastner, David; Coulter, Michael; Roumis, Demetris; Frank, Loren (2022) Gillespie et al (2021) Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000116">*[DANDI:000116](https://dandiarchive.org/dandiset/000116/draft)*: **Test_upload_LiZhang_SpinalCord**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, Guang-Wei (2022) Test_upload_LiZhang_SpinalCord*

---

<a id="000117">*[DANDI:000117](https://dandiarchive.org/dandiset/000117/draft)*: **1U01MH116990-01_July_2021**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **197**, total size (MB): **142.55**

- Keywords: **spinal cord**, **patch-clamp**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Zhang, Guang-Wei (2022) 1U01MH116990-01_July_2021*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000117_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/feaa8040-8f0b-47fb-abc2-6d50a434fd13) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000117/draft/files?location=sub-20210511003-2021-05-11-0012%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/feaa8040-8f0b-47fb-abc2-6d50a434fd13/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/29817159-63a3-4da4-986d-ff751ee1b067) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000117/draft/files?location=sub-20210615003-2021-06-15-0018%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/29817159-63a3-4da4-986d-ff751ee1b067/download/) 
---

<a id="000118">*[DANDI:000118](https://dandiarchive.org/dandiset/000118/draft)*: **user test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Dichter, Ben (2023) user test*

---

<a id="000119">*[DANDI:000119](https://dandiarchive.org/dandiset/000119/draft)*: **ble**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2022) ble*

---

<a id="000120">*[DANDI:000120](https://dandiarchive.org/dandiset/000120/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test*

---

<a id="000121">*[DANDI:000121](https://dandiarchive.org/dandiset/000121/draft)*: **Structure and variability of delay activity in premotor cortex**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Even-Chen, Nir; Sheffer, Blue; Vyas, Saurabh; Ryu, Stephen; Shenoy, Krishna (2022) Structure and variability of delay activity in premotor cortex*

---

<a id="000122">*[DANDI:000122](https://dandiarchive.org/dandiset/000122/draft)*: **Human fNIRS recordings of motor cortex during finger-tapping task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **5**, total size (MB): **49.9**

- Keywords: **fNIRS**, **Haemodynamics**, **Motor Cortex**, **Finger Tapping Task**

- Variables measured: 

- Source paper: *Erat Sleiter, Darin (2022) Human fNIRS recordings of motor cortex during finger-tapping task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000122_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 8.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/3af36329-5e0c-4c20-a283-87207b5569f1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000122/draft/files?location=sub-P2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3af36329-5e0c-4c20-a283-87207b5569f1/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 10.7 MB | 
[File info](https://api.dandiarchive.org/api/assets/911c75ab-51b5-4caa-b930-911b89d2c990) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000122/draft/files?location=sub-P5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/911c75ab-51b5-4caa-b930-911b89d2c990/download/) 
---

<a id="000123">*[DANDI:000123](https://dandiarchive.org/dandiset/000123/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Choudhury, Roni (2022) test*

---

<a id="000124">*[DANDI:000124](https://dandiarchive.org/dandiset/000124/draft)*: **footest**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Choudhury, Roni (2022) footest*

---

<a id="000125">*[DANDI:000125](https://dandiarchive.org/dandiset/000125/draft)*: **Neural population dynamics during reaching: analysis dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Churchland, Mark; Kauffman, Matthew; Cunningham, John; Foster, Justin; Shenoy, Krishna; Ryu, Stephen; Nuyujukian, Paul (2022) Neural population dynamics during reaching: analysis dataset*

---

<a id="000126">*[DANDI:000126](https://dandiarchive.org/dandiset/000126/draft)*: **NWB API Test Data**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **5**, total size (MB): **167.06**

- Species: **House mouse**

- Variables measured: **ProcessingModule**

- Source paper: *Ly, Ryan (2022) NWB API Test Data*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000126_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 36.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/e303dfac-48b1-44de-a847-9cf6154d5ad7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000126/draft/files?location=sub-1001658946%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e303dfac-48b1-44de-a847-9cf6154d5ad7/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000127">*[DANDI:000127](https://dandiarchive.org/dandiset/000127/draft)*: **Area2_Bump: macaque somatosensory area 2 spiking activity during reaching with perturbations**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **2**, total size (MB): **1,823.37**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **ElectrodeGroup**, **Units**, **SpatialSeries**, **ProcessingModule**

- Source paper: *Chowdhury, Raeed; Miller, Lee (2022) Area2_Bump: macaque somatosensory area 2 spiking activity during reaching with perturbations*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000128">*[DANDI:000128](https://dandiarchive.org/dandiset/000128/draft)*: **MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **694.0**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000128_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 690.61 MB | 
[File info](https://api.dandiarchive.org/api/assets/26e85f09-39b7-480f-b337-278a8f034007) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000128/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/26e85f09-39b7-480f-b337-278a8f034007/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000129">*[DANDI:000129](https://dandiarchive.org/dandiset/000129/draft)*: **MC_RTT: macaque motor cortex spiking activity during self-paced reaching**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **50.97**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ElectrodeGroup**, **ProcessingModule**

- Source paper: *O'Doherty, Joseph (2022) MC_RTT: macaque motor cortex spiking activity during self-paced reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000129_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 49.76 MB | 
[File info](https://api.dandiarchive.org/api/assets/2ae6bf3c-788b-4ece-8c01-4b4a5680b25b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000129/draft/files?location=sub-Indy%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2ae6bf3c-788b-4ece-8c01-4b4a5680b25b/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000130">*[DANDI:000130](https://dandiarchive.org/dandiset/000130/draft)*: **DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **15.67**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**

- Source paper: *Sohn, Hansem; Jazayeri, Mehrdad (2022) DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000130_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 14.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/c90cbccc-31a5-4815-88e6-822d8c5ca68c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000130/draft/files?location=sub-Haydn%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c90cbccc-31a5-4815-88e6-822d8c5ca68c/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000131">*[DANDI:000131](https://dandiarchive.org/dandiset/000131/draft)*: **Nestdesktop PK**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Nestdesktop PK*

---

<a id="000132">*[DANDI:000132](https://dandiarchive.org/dandiset/000132/draft)*: **Neurex Summer School**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Neurex Summer School*

---

<a id="000133">*[DANDI:000133](https://dandiarchive.org/dandiset/000133/draft)*: **nest dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) nest dataset*

---

<a id="000134">*[DANDI:000134](https://dandiarchive.org/dandiset/000134/draft)*: **neurex**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) neurex*

---

<a id="000135">*[DANDI:000135](https://dandiarchive.org/dandiset/000135/draft)*: **Test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Durieux, Laura (2022) Test*

---

<a id="000136">*[DANDI:000136](https://dandiarchive.org/dandiset/000136/draft)*: **NEST**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) NEST*

---

<a id="000137">*[DANDI:000137](https://dandiarchive.org/dandiset/000137/draft)*: **Neurex Summer School 2021**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Neurex Summer School 2021*

---

<a id="000138">*[DANDI:000138](https://dandiarchive.org/dandiset/000138/draft)*: **MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **149.39**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze_Large: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000138_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 148.59 MB | 
[File info](https://api.dandiarchive.org/api/assets/e67b57b2-e9ad-4d95-b9e3-1262997360dc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000138/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e67b57b2-e9ad-4d95-b9e3-1262997360dc/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000139">*[DANDI:000139](https://dandiarchive.org/dandiset/000139/draft)*: **MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **77.3**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze_Medium: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000139_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 76.6 MB | 
[File info](https://api.dandiarchive.org/api/assets/7ef450a8-8684-42e2-8598-cd38ca2b2e50) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000139/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7ef450a8-8684-42e2-8598-cd38ca2b2e50/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000140">*[DANDI:000140](https://dandiarchive.org/dandiset/000140/draft)*: **MC_Maze_Small: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **29.9**

- Species: **Rhesus monkey**

- Keywords: **Neural Latents Benchmark**, **NLB**

- Variables measured: **Units**, **ProcessingModule**

- Source paper: *Churchland, Mark; Kaufman, Matthew (2022) MC_Maze_Small: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000140_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 29.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/7821971e-c6a4-4568-8773-1bfa205c13f8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000140/draft/files?location=sub-Jenkins%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7821971e-c6a4-4568-8773-1bfa205c13f8/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000141">*[DANDI:000141](https://dandiarchive.org/dandiset/000141/draft)*: **TravelingDirection_2021**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) TravelingDirection_2021*

---

<a id="000142">*[DANDI:000142](https://dandiarchive.org/dandiset/000142/draft)*: **20210923_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **717**, total size (MB): **26,800.03**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortical**

- Variables measured: **ProcessingModule**

- Source paper: *20210923_AIBS_Patchseq_human (2023).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000142_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 12.72 MB | 
[File info](https://api.dandiarchive.org/api/assets/7efbccf6-b551-4919-a2a2-00790d80bedc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000142/draft/files?location=sub-707724503%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7efbccf6-b551-4919-a2a2-00790d80bedc/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 13.49 MB | 
[File info](https://api.dandiarchive.org/api/assets/1eec66c2-c7f4-4c43-8204-c9e5fbc09f8d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000142/draft/files?location=sub-643277950%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1eec66c2-c7f4-4c43-8204-c9e5fbc09f8d/download/) 
---

<a id="000143">*[DANDI:000143](https://dandiarchive.org/dandiset/000143/draft)*: **IHC Validation Data**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **50**, total size (MB): **10.0**

- Variables measured: 

- Source paper: *DeLorenzo, Lauren (2022) IHC Validation Data*

---

<a id="000144">*[DANDI:000144](https://dandiarchive.org/dandiset/000144/draft)*: **croat-test**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **2**, total size (MB): **589.06**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**, **TwoPhotonSeries**

- Source paper: *Roat, Chris (2022) croat-test*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000144_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 524.48 MB | 
[File info](https://api.dandiarchive.org/api/assets/bd754a60-c4a8-43fc-b514-87eb4511f29d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000144/draft/files?location=sub-8675309%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/bd754a60-c4a8-43fc-b514-87eb4511f29d/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000145">*[DANDI:000145](https://dandiarchive.org/dandiset/000145/draft)*: **Test 2**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Roat, Chris (2022) Test 2*

---

<a id="000146">*[DANDI:000146](https://dandiarchive.org/dandiset/000146/draft)*: **NYB**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) NYB*

---

<a id="000147">*[DANDI:000147](https://dandiarchive.org/dandiset/000147/draft)*: **PPC_Finger: human posterior parietal cortex recordings during attempted finger movements**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **10**, total size (MB): **77.67**

- Species: **Homo sapiens - Human**

- Keywords: **PPC**, **human**, **finger**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Guan, Charles; Aflalo, Tyson; Zhang, Carey; Andersen, Richard (2022) PPC_Finger: human posterior parietal cortex recordings during attempted finger movements*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000147_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 5.68 MB | 
[File info](https://api.dandiarchive.org/api/assets/d4c985da-5c04-4c39-874b-0c6e22598716) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000147/draft/files?location=sub-P1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d4c985da-5c04-4c39-874b-0c6e22598716/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 6.1 MB | 
[File info](https://api.dandiarchive.org/api/assets/675e49ed-04f2-4281-a4cb-5a1d3363e773) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000147/draft/files?location=sub-P1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/675e49ed-04f2-4281-a4cb-5a1d3363e773/download/) 
---

<a id="000148">*[DANDI:000148](https://dandiarchive.org/dandiset/000148/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 01_Oct_2021**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **46**, total size (MB): **929.64**

- Species: **Mus musculus - House mouse**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Zhang, Guang-Wei; Tao, Can; Peng, Bo (2022) Electrophysiological properties of adult mouse spinal cord neurons - 01_Oct_2021*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000148_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 10.26 MB | 
[File info](https://api.dandiarchive.org/api/assets/96cab2be-2416-4fae-8204-618983fe5fcc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000148/draft/files?location=sub-20210728003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/96cab2be-2416-4fae-8204-618983fe5fcc/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 10.42 MB | 
[File info](https://api.dandiarchive.org/api/assets/89f37b43-76e0-45a3-8c88-3ce7f640016c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000148/draft/files?location=sub-20210709003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/89f37b43-76e0-45a3-8c88-3ce7f640016c/download/) 
---

<a id="000149">*[DANDI:000149](https://dandiarchive.org/dandiset/000149/draft)*: **IBL ephys data**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **4**, total size (MB): **1,980,839.95**

- Species: **House mouse**

- Variables measured: **Position**, **Units**, **BehavioralTimeSeries**, **ElectrodeGroup**

- Source paper: *International Brain Laboratory (2023) IBL ephys data*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000150">*[DANDI:000150](https://dandiarchive.org/dandiset/000150/draft)*: **test_release_openscope**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test_release_openscope*

---

<a id="000151">*[DANDI:000151](https://dandiarchive.org/dandiset/000151/draft)*: **OpenScope_Credit_assignement_raw_test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Lecoq, Jerome (2022) OpenScope_Credit_assignement_raw_test*

---

<a id="000152">*[DANDI:000152](https://dandiarchive.org/dandiset/000152/draft)*: **test_workshop**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2022) test_workshop*

---

<a id="000153">*[DANDI:000153](https://dandiarchive.org/dandiset/000153/draft)*: **IEDs**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *H Smith, Elliot (2022) IEDs*

---

<a id="000154">*[DANDI:000154](https://dandiarchive.org/dandiset/000154/draft)*: **test dandi workshop**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test dandi workshop*

---

<a id="000155">*[DANDI:000155](https://dandiarchive.org/dandiset/000155/draft)*: **dandi workshop djd**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *denman, daniel (2022) dandi workshop djd*

---

<a id="000156">*[DANDI:000156](https://dandiarchive.org/dandiset/000156/draft)*: **dandi workshop to be deleted**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **mouse**

- Source paper: *Chrapkiewicz, Radek (2022) dandi workshop to be deleted*

---

<a id="000157">*[DANDI:000157](https://dandiarchive.org/dandiset/000157/draft)*: **xiaoai**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) xiaoai*

---

<a id="000158">*[DANDI:000158](https://dandiarchive.org/dandiset/000158/draft)*: **My Project**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *C. Petersen, Peter (2022) My Project*

---

<a id="000159">*[DANDI:000159](https://dandiarchive.org/dandiset/000159/draft)*: **dandi workshop**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) dandi workshop*

---

<a id="000160">*[DANDI:000160](https://dandiarchive.org/dandiset/000160/draft)*: **Test_G**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Test_G*

---

<a id="000161">*[DANDI:000161](https://dandiarchive.org/dandiset/000161/draft)*: **VD Dandi Workshop Test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) VD Dandi Workshop Test*

---

<a id="000162">*[DANDI:000162](https://dandiarchive.org/dandiset/000162/draft)*: **Shin test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Shin test*

---

<a id="000163">*[DANDI:000163](https://dandiarchive.org/dandiset/000163/draft)*: **xx**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) xx*

---

<a id="000164">*[DANDI:000164](https://dandiarchive.org/dandiset/000164/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) test*

---

<a id="000165">*[DANDI:000165](https://dandiarchive.org/dandiset/000165/draft)*: **Aery Jones et al (2021) Dentate Gyrus and CA3 GABAergic Interneurons Bidirectionally Modulate Signatures of Internal and External Drive to CA1**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **572**, total size (MB): **98,043.54**

- Species: **House mouse**

- Keywords: **hippocampus**, **mouse**, **LFP**

- Variables measured: **Units**, **Position**, **LFP**, **SpatialSeries**, **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Aery Jones, Emily; Rao, Antara; Zilberter, Misha; Djukic, Biljana; Gillespie, Anna K.; Koutsodendris, Nicole; Nelson, Maxine; Yoon, Seo Yeon; Huang, Ky; Yuan, Heidi; Gill, Theodore M.; Huang, Yadong; Frank, Loren M. (2022) Aery Jones et al (2021) Dentate Gyrus and CA3 GABAergic Interneurons Bidirectionally Modulate Signatures of Internal and External Drive to CA1*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000165_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 47.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/b560b456-3473-42dd-9fe2-e7f3cc506731) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000165/draft/files?location=sub-Parsley%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b560b456-3473-42dd-9fe2-e7f3cc506731/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 51.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/e3a976f9-505f-477f-8ab8-db901dc606b6) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000165/draft/files?location=sub-Sage%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e3a976f9-505f-477f-8ab8-db901dc606b6/download/) 
---

<a id="000166">*[DANDI:000166](https://dandiarchive.org/dandiset/000166/draft)*: **Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **19**, total size (MB): **787,191.91**

- Species: **House mouse**

- Keywords: **current source density **, **laminar recordings **, **cortex**, **electrophysiology**

- Variables measured: **ElectrodeGroup**, **Units**, **LFP**

- Source paper: *Senzai, Yuta; Fernandez-Ruiz, Antonio; Buzsáki, György (2022) Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000167">*[DANDI:000167](https://dandiarchive.org/dandiset/000167/draft)*: **Two photon calcium imaging of mice piriform cortex under passive odor presentation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **6**, total size (MB): **1,218.41**

- Species: **Mus musculus - House mouse**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**, **ImagingPlane**, **OpticalChannel**

- Source paper: *Daste, Simon; Pierré, Andrea; Pham, Tuan (2023) Two photon calcium imaging of mice piriform cortex under passive odor presentation*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000167_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 190.53 MB | 
[File info](https://api.dandiarchive.org/api/assets/4b934f5d-bb2c-425e-ac99-bb40f22302ae) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000167/draft/files?location=sub-7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4b934f5d-bb2c-425e-ac99-bb40f22302ae/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 201.35 MB | 
[File info](https://api.dandiarchive.org/api/assets/3b16b193-7afa-4479-ad5d-cfb09f5f6776) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000167/draft/files?location=sub-164%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3b16b193-7afa-4479-ad5d-cfb09f5f6776/download/) 
---

<a id="000168">*[DANDI:000168](https://dandiarchive.org/dandiset/000168/draft)*: **Simultaneous loose seal cell-attached recordings  and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **170**, total size (MB): **1,379,111.6**

- Species: **Mus musculus - House mouse**

- Keywords: **2-photon**, **visual cortex**, **calcium**, **spike**, **action potential**, **layer 2**, **AAV**, **adeno-associated virus**, **jGCaMP8s**, **jGCaMP8m**, **jGCaMP8f**, **jGCaMP7f**, **XCaMP-Gf**

- Variables measured: **PlaneSegmentation**, **CurrentClampStimulusSeries**, **CurrentClampSeries**, **TwoPhotonSeries**, **ProcessingModule**, **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Rozsa, Marton; Liang, Yajie; Zhang, Yan; Hasseman, Jeremy; Kolb, Ilya; Looger, Loren; Svoboda, Karel; HHMI (2022) Simultaneous loose seal cell-attached recordings  and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000168_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1430.99 MB | 
[File info](https://api.dandiarchive.org/api/assets/026e2006-8779-4d04-83db-7590b47c1afa) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000168/draft/files?location=XCaMPgf%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/026e2006-8779-4d04-83db-7590b47c1afa/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 1709.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/c442f0bf-49e1-46b8-b9c8-e9d1d7cdcc35) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000168/draft/files?location=jGCaMP8f%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c442f0bf-49e1-46b8-b9c8-e9d1d7cdcc35/download/) 
---

<a id="000169">*[DANDI:000169](https://dandiarchive.org/dandiset/000169/draft)*: **Milti-probe Neuropixels recordings in mouse visual system (additional data)**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) Milti-probe Neuropixels recordings in mouse visual system (additional data)*

---

<a id="000170">*[DANDI:000170](https://dandiarchive.org/dandiset/000170/draft)*: **CRACK**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *,  (2022) CRACK*

---

<a id="000171">*[DANDI:000171](https://dandiarchive.org/dandiset/000171/draft)*: **Test 1**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Yu, Kai (2022) Test 1*

---

<a id="000172">*[DANDI:000172](https://dandiarchive.org/dandiset/000172/draft)*: **UHN whole-cell excitability recordings from mouse cortical neurons**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **excitability**, **cortex**, **mouse**

- Source paper: *Howard, Derek; Chameh, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell excitability recordings from mouse cortical neurons*

---

<a id="000173">*[DANDI:000173](https://dandiarchive.org/dandiset/000173/draft)*: **Neural Spiking Data in Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **118**, total size (MB): **240.96**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **Ultrasound**, **Plasticity**, **Rat**, **tFUS**, **Somatosensory Cortex**

- Variables measured: **Units**

- Source paper: *Ramachandran, Sandhya; Carnegie Mellon University; Niu, Xiaodan; Yu, Kai; He, Bin (2022) Neural Spiking Data in Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000173_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/748b0311-ec11-49ef-a9c2-e7b1afef72dc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000173/draft/files?location=sub-BH279%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/748b0311-ec11-49ef-a9c2-e7b1afef72dc/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/cebb65cf-e933-470d-87b4-6660eac86b3e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000173/draft/files?location=sub-BH269%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/cebb65cf-e933-470d-87b4-6660eac86b3e/download/) 
---

<a id="000206">*[DANDI:000206](https://dandiarchive.org/dandiset/000206/draft)*: **Visual cortical activity in mice performing naturalistic virtual foraging task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1**, total size (MB): **118.36**

- Species: **House mouse**

- Variables measured: **SpatialSeries**, **ImagingPlane**, **Position**, **OpticalChannel**

- Source paper: *Smith, Spencer; McGreal, Ryan; Canzano, Joseph (2022) Visual cortical activity in mice performing naturalistic virtual foraging task*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000206_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 118.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/e0e142bc-cf1e-4a38-8d24-b54111c404db) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000206/draft/files?location=sub-TIGRE296%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e0e142bc-cf1e-4a38-8d24-b54111c404db/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000207">*[DANDI:000207](https://dandiarchive.org/dandiset/000207/draft)*: **Data for: Neurons detect cognitive boundaries to structure episodic memories in humans (Zheng et al., 2022, Nat Neuro in press)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **19**, total size (MB): **50.31**

- Species: **Homo sapiens - Human**

- Keywords: **human single neuron**, **hippocampus**, **episodic memory**, **event segmentation**, **amygdala**, **parahippocampal gyrus**, **cognitive boundaries**, **continuous experience**, **ROH consortium**

- Variables measured: **ElectrodeGroup**, **Units**

- Source paper: *Zheng, Jie; Schjetnan, Andrea; Yebra, Mar; Gomes, Bernard; Mosher, Clayton; Kalia, Suneil; Valiante, Taufik; Mamelak, Adam; Kreiman, Gabriel; Rutishauser, Ueli (2023) Data for: Neurons detect cognitive boundaries to structure episodic memories in humans (Zheng et al., 2022, Nat Neuro in press)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000207_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/88e33ca7-2e46-411f-8f5f-1826dfef5bbc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000207/draft/files?location=sub-6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/88e33ca7-2e46-411f-8f5f-1826dfef5bbc/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 1.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/22a64207-e573-4324-99ae-345f8a71b7b9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000207/draft/files?location=sub-10%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/22a64207-e573-4324-99ae-345f8a71b7b9/download/) 
---

<a id="000208">*[DANDI:000208](https://dandiarchive.org/dandiset/000208/draft)*: **UHN_mouse_L5_patchclamp**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *, Derek (2022) UHN_mouse_L5_patchclamp*

---

<a id="000209">*[DANDI:000209](https://dandiarchive.org/dandiset/000209/draft)*: **20211223_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **291**, total size (MB): **11,109.21**

- Species: **Human**

- Keywords: **Patch-seq**, **human**, **neocortical**

- Variables measured: **ProcessingModule**

- Source paper: *Wakeman, Wayne; Kalmbach, Brian; Lein, Ed; Chartrand, Thomas (2023) 20211223_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000209_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 16.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/2d665bd8-9b7b-4315-be44-cc48fb91a4a7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000209/draft/files?location=sub-731978186%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2d665bd8-9b7b-4315-be44-cc48fb91a4a7/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 19.03 MB | 
[File info](https://api.dandiarchive.org/api/assets/10e78b16-a771-44e4-bd9a-395cade15c84) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000209/draft/files?location=sub-1032184063%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/10e78b16-a771-44e4-bd9a-395cade15c84/download/) 
---

<a id="000210">*[DANDI:000210](https://dandiarchive.org/dandiset/000210/draft)*: **Visual cortical activity in mice performing naturalistic virtual foraging task**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Canzano, Joe (2022) Visual cortical activity in mice performing naturalistic virtual foraging task*

---

<a id="000211">*[DANDI:000211](https://dandiarchive.org/dandiset/000211/draft)*: **UHN whole-cell excitability recordings from human cortical neurons**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **excitability**, **human**, **cortex**

- Source paper: *Howard, Derek; Chameh, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell excitability recordings from human cortical neurons*

---

<a id="000212">*[DANDI:000212](https://dandiarchive.org/dandiset/000212/draft)*: **Tracking of Drosophila during egg-laying decisions**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1013**, total size (MB): **9,004.4**

- Species: **Drosophila melanogaster - Fruit fly**

- Keywords: **Drosophila**, **egg laying**, **flies**, **decision making**, **internal expectation**

- Variables measured: **Position**, **ProcessingModule**, **SpatialSeries**

- Source paper: *Vijayan, Vikram; Maimon, Gaby (2023) Tracking of Drosophila during egg-laying decisions*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000212_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 7.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/b53cc570-a02b-41c8-bce2-7351816b76b2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000212/draft/files?location=sub-0-200-Dop1R2-mutant-2-fly#-21%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b53cc570-a02b-41c8-bce2-7351816b76b2/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 7.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/8a916887-b90e-4de4-9895-e2bed5adaf1b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000212/draft/files?location=sub-0-200-Dop1R2-mutant-2-fly#-20%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8a916887-b90e-4de4-9895-e2bed5adaf1b/download/) 
---

<a id="000213">*[DANDI:000213](https://dandiarchive.org/dandiset/000213/draft)*: **Transformation of a Spatial Map across the Hippocampal-Lateral Septal Circuit**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **67**, total size (MB): **1,527,009.27**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **hippocampus**, **lateral septum**, **electrophysiology**

- Variables measured: **Position**, **CompassDirection**, **ElectricalSeries**, **LFP**, **Units**, **SpatialSeries**

- Source paper: *Tingley, David; Buzsáki, Gyórgy (2022) Transformation of a Spatial Map across the Hippocampal-Lateral Septal Circuit*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000213_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 746.95 MB | 
[File info](https://api.dandiarchive.org/api/assets/d09a9733-41d8-4696-86bb-e041668247b6) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000213/draft/files?location=sub-DT7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d09a9733-41d8-4696-86bb-e041668247b6/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 826.17 MB | 
[File info](https://api.dandiarchive.org/api/assets/1d183c70-082d-4ce8-b017-05620cc9254f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000213/draft/files?location=sub-DT5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1d183c70-082d-4ce8-b017-05620cc9254f/download/) 
---

<a id="000214">*[DANDI:000214](https://dandiarchive.org/dandiset/000214/draft)*: **Jan_2022_DANDI**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, Guang-Wei (2022) Jan_2022_DANDI*

---

<a id="000215">*[DANDI:000215](https://dandiarchive.org/dandiset/000215/draft)*: **1U01MH116990-01_Jan_2022**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **spinal cord **

- Source paper: *Zhang, Guang-Wei (2022) 1U01MH116990-01_Jan_2022*

---

<a id="000216">*[DANDI:000216](https://dandiarchive.org/dandiset/000216/draft)*: **1U01MH116990-01_Jan_2022**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, Guang-Wei (2022) 1U01MH116990-01_Jan_2022*

---

<a id="000217">*[DANDI:000217](https://dandiarchive.org/dandiset/000217/draft)*: **Sniff-synchronized, gradient-guided olfactory search by freely moving mice -- Behavioral Dataset**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1121**, total size (MB): **2,152.04**

- Species: **Mus musculus - House mouse**

- Variables measured: 

- Source paper: *Findley, Teresa; Wyrick, David G; Cramer, Jennifer L; Brown, Morgan A; Holcomb, Blake; Attey, Robin; Yeh, Dorian; Monasevitch, Eric; Nouboussi, Nelly; Cullen, Isabelle; Songco, Jeremea O; King, Jared F; Ahmadian, Yashar; Smear, Matt (2022) Sniff-synchronized, gradient-guided olfactory search by freely moving mice -- Behavioral Dataset*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000217_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/32be659d-80fa-4021-8d6e-4b8cb7e21c2c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000217/draft/files?location=sub-Mouse 2071%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/32be659d-80fa-4021-8d6e-4b8cb7e21c2c/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/d3e786a8-787c-4a80-9dd6-ffeca84a8577) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000217/draft/files?location=sub-Mouse 2083%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d3e786a8-787c-4a80-9dd6-ffeca84a8577/download/) 
---

<a id="000218">*[DANDI:000218](https://dandiarchive.org/dandiset/000218/draft)*: **Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **98**, total size (MB): **1,512,863.48**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **hippocampus**, **lateral septum**, **electrophyisology**

- Variables measured: **LFP**, **Units**, **ProcessingModule**, **Position**, **CompassDirection**, **ElectricalSeries**, **SpatialSeries**

- Source paper: *Tingley, David; Buzáki, Gyórgy (2022) Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000218_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 570.69 MB | 
[File info](https://api.dandiarchive.org/api/assets/a6cf3b13-1220-415c-93ad-05d0eeff0f46) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000218/draft/files?location=sub-DT7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a6cf3b13-1220-415c-93ad-05d0eeff0f46/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 638.46 MB | 
[File info](https://api.dandiarchive.org/api/assets/5eb882bd-9242-47bd-bcd0-da548afe01d1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000218/draft/files?location=sub-DT5%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/5eb882bd-9242-47bd-bcd0-da548afe01d1/download/) 
---

<a id="000219">*[DANDI:000219](https://dandiarchive.org/dandiset/000219/draft)*: **Two photon calcium imaging in the CA1 region of the hippocampus in neonatal mice.**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **62**, total size (MB): **73,147.04**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralEpochs**, **PlaneSegmentation**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Dard, Robin (2022) Two photon calcium imaging in the CA1 region of the hippocampus in neonatal mice*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000219_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 813.61 MB | 
[File info](https://api.dandiarchive.org/api/assets/30aee0ab-a751-4646-9e13-6032be28a0df) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000219/draft/files?location=sub-210226-210308-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/30aee0ab-a751-4646-9e13-6032be28a0df/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 814.67 MB | 
[File info](https://api.dandiarchive.org/api/assets/113a60b6-bfde-4c63-b4cf-10a7821b48c5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000219/draft/files?location=sub-210226-210307-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/113a60b6-bfde-4c63-b4cf-10a7821b48c5/download/) 
---

<a id="000220">*[DANDI:000220](https://dandiarchive.org/dandiset/000220/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 25_Jan_2022**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **34**, total size (MB): **1,202.85**

- Species: **Mus musculus - House mouse**

- Variables measured: 

- Source paper: *Zhang, Guang-Wei; Tao, Can; Peng, Bo (2022) Electrophysiological properties of adult mouse spinal cord neurons - 25_Jan_2022*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000220_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 12.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/55463159-6466-48ac-9a7d-c05e2624ef3f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000220/draft/files?location=sub-20190117002%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/55463159-6466-48ac-9a7d-c05e2624ef3f/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 12.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/161cdf76-8cd7-45ce-9551-6a0d15870edf) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000220/draft/files?location=sub-20190315001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/161cdf76-8cd7-45ce-9551-6a0d15870edf/download/) 
---

<a id="000221">*[DANDI:000221](https://dandiarchive.org/dandiset/000221/draft)*: **A midbrain-thalamus-cortex circuit reorganizes cortical dynamics to initiate movement**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **263**, total size (MB): **4,422.55**

- Species: **Mus musculus - House mouse**

- Keywords: **Midbrain**, **ALM**, **motor planning**, **movement initiation**

- Variables measured: **SpikeEventSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Inagaki, Hidehiko; Chen, Susu; Svoboda, Karel (2022) A midbrain-thalamus-cortex circuit reorganizes cortical dynamics to initiate movement*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000221_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.41 MB | 
[File info](https://api.dandiarchive.org/api/assets/f02ab674-44f5-4c87-8679-04fa049c7674) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000221/draft/files?location=sub-HI204%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f02ab674-44f5-4c87-8679-04fa049c7674/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/de094939-990a-4d6e-af29-dde24936420c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000221/draft/files?location=sub-SC020%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/de094939-990a-4d6e-af29-dde24936420c/download/) 
---

<a id="000222">*[DANDI:000222](https://dandiarchive.org/dandiset/000222/draft)*: **O'Hare et al 2022**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **neuroscience, dendrites, hippocampus, mouse, plasticity, endoplasmic reticulum, calcium**

- Source paper: *O'Hare, Justin (2022) O'Hare et al 2022*

---

<a id="000223">*[DANDI:000223](https://dandiarchive.org/dandiset/000223/draft)*: **Inferring monosynaptic connections from paired spine calcium imaging and large-scale recording of extracellular spiking**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **20**, total size (MB): **84,273.72**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **calcium imaging; extracellular recordings; HD-MEA; spike sorting; dendritic spines**

- Variables measured: **PlaneSegmentation**, **ElectrodeGroup**, **ProcessingModule**, **ElectricalSeries**, **TwoPhotonSeries**, **Units**

- Source paper: *Xue, Xiaohan; Buccino, Alessio; Kumar, Sreedhar Saseendran; Hierlemann, Andreas; Bartram, Julian (2022) Inferring monosynaptic connections from paired spine calcium imaging and large-scale recording of extracellular spiking*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000225">*[DANDI:000225](https://dandiarchive.org/dandiset/000225/draft)*: **Neural and behavioral**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Khoury, Christine (2022) Neural and behavioral*

---

<a id="000226">*[DANDI:000226](https://dandiarchive.org/dandiset/000226/draft)*: **Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **60**, total size (MB): **13,745.15**

- Species: **Mus musculus - House mouse**

- Variables measured: **Units**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Severson, Kyle; Xu, Duo; Van de Loo, Margaret; Bai, Ling; Ginty, David D; O'Connor, Daniel H (2023) Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000226_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 19.48 MB | 
[File info](https://api.dandiarchive.org/api/assets/9c90c18a-8e66-4644-a402-e5f849fc08a1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000226/draft/files?location=sub-KSt91%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/9c90c18a-8e66-4644-a402-e5f849fc08a1/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 19.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/0cfad5c5-e44b-424d-bffc-da64ac30fe12) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000226/draft/files?location=sub-KSt119%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0cfad5c5-e44b-424d-bffc-da64ac30fe12/download/) 
---

<a id="000227">*[DANDI:000227](https://dandiarchive.org/dandiset/000227/draft)*: **Electrophysiological recordings in protein hunger neurons of Drosophila Melanogaster**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Liu, Qili (2022) Electrophysiological recordings in protein hunger neurons of Drosophila Melanogaster*

---

<a id="000228">*[DANDI:000228](https://dandiarchive.org/dandiset/000228/draft)*: **20220330_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **91**, total size (MB): **5,816.16**

- Species: **Homo sapiens - Human**

- Keywords: **Patch-seq**, **human**, **neocortical**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Chartrand, Thomas; Kalmbach, Brian; Molnar, Gabor; Tamas, Gabor; Lein, Ed (2022) 20220330_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000228_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 35.66 MB | 
[File info](https://api.dandiarchive.org/api/assets/bdc5f608-caa8-4ac0-a70d-b03a1739ba66) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000228/draft/files?location=sub-H18-28-022%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/bdc5f608-caa8-4ac0-a70d-b03a1739ba66/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 43.37 MB | 
[File info](https://api.dandiarchive.org/api/assets/e42540ff-da70-4dfa-aa9e-05b8512e1e20) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000228/draft/files?location=sub-H20-28-022%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e42540ff-da70-4dfa-aa9e-05b8512e1e20/download/) 
---

<a id="000229">*[DANDI:000229](https://dandiarchive.org/dandiset/000229/draft)*: **xxx**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Findley, Teresa (2022) xxx*

---

<a id="000230">*[DANDI:000230](https://dandiarchive.org/dandiset/000230/draft)*: **Jacobsen 2022**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **9**, total size (MB): **244.97**

- Species: **Mus musculus - House mouse**

- Variables measured: **CompassDirection**, **Units**, **ElectrodeGroup**, **SpatialSeries**, **ElectricalSeries**, **BehavioralTimeSeries**, **ProcessingModule**, **LFP**, **Position**

- Source paper: *Jacobsen, R Irene; Nair, Rajeevkumar R; Obenhaus, Horst A; Donato, Flavio; Slettmoen, Torstein; Moser, May-Britt; Moser, Edvard I (2022) Jacobsen 2022*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000230_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 24.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/a8f7ef2e-c311-44d8-a72b-2d7bc7e5dc09) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000230/draft/files?location=sub-70375%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a8f7ef2e-c311-44d8-a72b-2d7bc7e5dc09/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 25.5 MB | 
[File info](https://api.dandiarchive.org/api/assets/d8e0ccfb-fc0d-4fd2-8b26-be8f187cc2c0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000230/draft/files?location=sub-58313%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d8e0ccfb-fc0d-4fd2-8b26-be8f187cc2c0/download/) 
---

<a id="000231">*[DANDI:000231](https://dandiarchive.org/dandiset/000231/draft)*: **A detailed behavioral, videographic, and neural dataset on object recognition in mice**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **4228**, total size (MB): **1,996,516.62**

- Species: **Mus musculus - House mouse**

- Keywords: **mouse behavior**, **whisker system**, **somatosensory cortex**, **barrel cortex**, **object recognition**, **shape discrimination**, **electrophysiology**, **pose tracking**, **population recordings**, **single unit recordings**

- Variables measured: **BehavioralTimeSeries**, **BehavioralEvents**, **ProcessingModule**, **Units**, **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Rodgers, Chris (2022) A detailed behavioral, videographic, and neural dataset on object recognition in mice*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000231_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 378.69 MB | 
[File info](https://api.dandiarchive.org/api/assets/2374f6b9-babe-4fbd-8cca-df4f8b4ec4c0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000231/draft/files?location=sub-KF119%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2374f6b9-babe-4fbd-8cca-df4f8b4ec4c0/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 382.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/d45acf3d-aaa9-4f70-ae5d-f70cbc411950) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000231/draft/files?location=sub-219CR%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d45acf3d-aaa9-4f70-ae5d-f70cbc411950/download/) 
---

<a id="000232">*[DANDI:000232](https://dandiarchive.org/dandiset/000232/draft)*: **Rule-based modulation of  a sensorimotor transformation across cortical areas**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **86**, total size (MB): **36,639.9**

- Species: **Mus musculus - House mouse**

- Variables measured: **LFP**, **Units**, **BehavioralTimeSeries**, **ElectrodeGroup**, **ProcessingModule**, **ElectricalSeries**

- Source paper: *Chang, Yi-Ting; OConnor, Daniel H (2022) Rule-based modulation of  a sensorimotor transformation across cortical areas*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000232_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 280.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/a1bf6c0a-f424-4491-84b6-596852a2fcae) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000232/draft/files?location=sub-JL005%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a1bf6c0a-f424-4491-84b6-596852a2fcae/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 284.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/a4385201-8913-442c-ba03-41150bf4172d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000232/draft/files?location=sub-YT071%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a4385201-8913-442c-ba03-41150bf4172d/download/) 
---

<a id="000233">*[DANDI:000233](https://dandiarchive.org/dandiset/000233/draft)*: **A metabolic function of the hippocampal sharp wave-ripple**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **345**, total size (MB): **12,320,920.24**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **glucose**, **ecephys **, **pharmacology**

- Variables measured: **ElectricalSeries**, **ProcessingModule**, **LFP**, **ElectrodeGroup**

- Source paper: *Tingley, David; McClain, Kathryn; Kaya, Ekin; Carpenter, Jordan; Buzsáki, György (2023) A metabolic function of the hippocampal sharp wave-ripple*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000233_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 18.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/7acfe0c2-1fc1-4060-a423-25ebdd0b3a11) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000233/draft/files?location=sub-CGM57%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7acfe0c2-1fc1-4060-a423-25ebdd0b3a11/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 19.76 MB | 
[File info](https://api.dandiarchive.org/api/assets/80ea45a5-c84c-4b18-aa1d-d9f6b4658c35) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000233/draft/files?location=sub-CGM41%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/80ea45a5-c84c-4b18-aa1d-d9f6b4658c35/download/) 
---

<a id="000235">*[DANDI:000235](https://dandiarchive.org/dandiset/000235/draft)*: **Thermoregulatory Responses Forebrain**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **8**, total size (MB): **30,614.34**

- Species: **Danio rerio - Zebra fish**

- Variables measured: **OpticalChannel**, **PlaneSegmentation**, **TwoPhotonSeries**, **ProcessingModule**, **BehavioralTimeSeries**, **ImagingPlane**

- Source paper: *Haesemeyer, Martin; Balakrishnan, Kaarthik (2023) Thermoregulatory Responses Forebrain*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000236">*[DANDI:000236](https://dandiarchive.org/dandiset/000236/draft)*: **Thermoregulatory Responses Midbrain**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **9**, total size (MB): **39,306.12**

- Species: **Danio rerio - Zebra fish**

- Variables measured: **BehavioralTimeSeries**, **TwoPhotonSeries**, **ImagingPlane**, **ProcessingModule**, **PlaneSegmentation**, **OpticalChannel**

- Source paper: *Haesemeyer, Martin; Balakrishnan, Kaarthik (2023) Thermoregulatory Responses Midbrain*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000237">*[DANDI:000237](https://dandiarchive.org/dandiset/000237/draft)*: **Thermoregulatory Responses Hindbrain**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **8**, total size (MB): **30,057.96**

- Species: **Danio rerio - Zebra fish**

- Variables measured: **OpticalChannel**, **TwoPhotonSeries**, **PlaneSegmentation**, **ImagingPlane**, **ProcessingModule**, **BehavioralTimeSeries**

- Source paper: *Haesemeyer, Martin (2023) Thermoregulatory Responses Hindbrain*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000238">*[DANDI:000238](https://dandiarchive.org/dandiset/000238/draft)*: **Thermoregulatory Responses Reticulospinal system**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **6**, total size (MB): **25,911.94**

- Species: **Danio rerio - Zebra fish**

- Variables measured: **OpticalChannel**, **BehavioralTimeSeries**, **TwoPhotonSeries**, **PlaneSegmentation**, **ImagingPlane**, **ProcessingModule**

- Source paper: *Haesemeyer, Martin; Schwinn, Sina (2023) Thermoregulatory Responses Reticulospinal system*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000239">*[DANDI:000239](https://dandiarchive.org/dandiset/000239/draft)*: **Cortical processing of flexible and context-dependent sensorimotor sequences**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **754**, total size (MB): **11,769.9**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralTimeSeries**, **Units**, **ProcessingModule**

- Source paper: *Xu, Duo; Chen, Yuxi; Dong, Mingyuan; Delgado, Angel M; Hughes, Natasha C; Zhang, Linghua; O'Connor, Daniel H (2023) Cortical processing of flexible and context-dependent sensorimotor sequences*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000239_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.25 MB | 
[File info](https://api.dandiarchive.org/api/assets/656d2d9f-01f5-41b7-8703-31a6a0840302) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000239/draft/files?location=sub-MX180602%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/656d2d9f-01f5-41b7-8703-31a6a0840302/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.26 MB | 
[File info](https://api.dandiarchive.org/api/assets/05096d27-a83c-427d-b88a-3801bcf9e63a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000239/draft/files?location=sub-MX180804%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/05096d27-a83c-427d-b88a-3801bcf9e63a/download/) 
---

<a id="000241">*[DANDI:000241](https://dandiarchive.org/dandiset/000241/draft)*: **ngff testing**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2022) ngff testing*

---

<a id="000243">*[DANDI:000243](https://dandiarchive.org/dandiset/000243/draft)*: **MRI of human ex vivo brainstem**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **4**, total size (MB): **3,055.09**

- Variables measured: 

- Source paper: *Johnson, G Allan; Calabrese, Evan; Ghosh, Satrajit (2022) MRI of human ex vivo brainstem*

---

<a id="000244">*[DANDI:000244](https://dandiarchive.org/dandiset/000244/draft)*: **One photon mesoscale calcium imaging of multiple cell types**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **33**, total size (MB): **1,068,310.24**

- Species: **Mus musculus - House mouse**

- Variables measured: **ImagingPlane**, **TwoPhotonSeries**, **OpticalChannel**

- Source paper: *O'Connor, Dave (2022) One photon mesoscale calcium imaging of multiple cell types*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000245">*[DANDI:000245](https://dandiarchive.org/dandiset/000245/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 22Q1_Ephys_DANDI**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **25**, total size (MB): **408.91**

- Species: **Mus musculus - House mouse**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Zhang, Guang-Wei; Tao, Can (2022) Electrophysiological properties of adult mouse spinal cord neurons - 22Q1_Ephys_DANDI*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000245_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 8.64 MB | 
[File info](https://api.dandiarchive.org/api/assets/2ff065c2-9991-4b46-a4d6-474f602b891e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000245/draft/files?location=sub-20220317004%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2ff065c2-9991-4b46-a4d6-474f602b891e/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 8.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/a8bec861-62fa-4f23-bd8a-5cdf83f1695b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000245/draft/files?location=sub-20220119003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a8bec861-62fa-4f23-bd8a-5cdf83f1695b/download/) 
---

<a id="000246">*[DANDI:000246](https://dandiarchive.org/dandiset/000246/draft)*: **developing CaMPARI3**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **978**, total size (MB): **2,108,455.63**

- Species: **Mus musculus - House mouse**

- Variables measured: **OpticalChannel**, **TwoPhotonSeries**, **PlaneSegmentation**, **ProcessingModule**, **ImagingPlane**

- Source paper: *Icardi, Jacob (2023) developing CaMPARI3*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000246_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 188.92 MB | 
[File info](https://api.dandiarchive.org/api/assets/eba75a10-6e3c-4c3f-b7d7-f8d95633f343) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000246/draft/files?location=sub-phpV7-6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/eba75a10-6e3c-4c3f-b7d7-f8d95633f343/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 260.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/c1bf3dcd-7615-4fc4-8f6e-d84a2aa53e78) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000246/draft/files?location=sub-mouse20-C1 -19degree%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c1bf3dcd-7615-4fc4-8f6e-d84a2aa53e78/download/) 
---

<a id="000247">*[DANDI:000247](https://dandiarchive.org/dandiset/000247/draft)*: **Calcium imaging of egg-laying related neurons in head-fixed Drosophila**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **194**, total size (MB): **30,300.18**

- Species: **Drosophila melanogaster - Fruit fly**

- Keywords: **Drosophila**, **egg laying**, **flies**, **decision making**, **rise-to-threshold**

- Variables measured: **ProcessingModule**

- Source paper: *Vijayan, Vikram; Maimon, Gaby (2023) Calcium imaging of egg-laying related neurons in head-fixed Drosophila*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000247_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 4.11 MB | 
[File info](https://api.dandiarchive.org/api/assets/0c6e778d-9b87-4fa4-8bd4-8a189fb534db) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000247/draft/files?location=sub-oviDNSS1-driving-GCaMP7f-fly-ID#6010%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0c6e778d-9b87-4fa4-8bd4-8a189fb534db/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 4.23 MB | 
[File info](https://api.dandiarchive.org/api/assets/3e047be3-d417-4f8e-81cd-5c44254f5cba) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000247/draft/files?location=sub-oviDNSS1-driving-GCaMP7f-fly-ID#7006%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3e047be3-d417-4f8e-81cd-5c44254f5cba/download/) 
---

<a id="000248">*[DANDI:000248](https://dandiarchive.org/dandiset/000248/draft)*: **Allen Institute Openscope - Illusion project**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **78**, total size (MB): **186,040.63**

- Species: **Mus musculus - House mouse**

- Variables measured: **LFP**, **ElectricalSeries**, **OptogeneticSeries**, **Units**, **ProcessingModule**

- Source paper: *Allen Institute Openscope - Illusion project (2024).*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000249">*[DANDI:000249](https://dandiarchive.org/dandiset/000249/draft)*: **Innate and plastic mechanisms for maternal behaviour in auditory cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **777**, total size (MB): **97,968.24**

- Species: **Mus musculus - House mouse**

- Keywords: **oxytocin**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **TwoPhotonSeries**

- Source paper: *Schiavo, Jennifer K.; Valtcheva, Silvana; Bair-Marshall, Chloe J.; Song, Soomin C.; Martin, Kathleen A.; Froemke, Robert C. (2023) Innate and plastic mechanisms for maternal behaviour in auditory cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000249_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 36.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/7f25d292-0365-4e7d-ae7b-68c8c2124615) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000249/draft/files?location=sub-NV106%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7f25d292-0365-4e7d-ae7b-68c8c2124615/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 38.08 MB | 
[File info](https://api.dandiarchive.org/api/assets/01fdbd6c-abef-4097-988f-270d45db5ffb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000249/draft/files?location=sub-NV33%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/01fdbd6c-abef-4097-988f-270d45db5ffb/download/) 
---

<a id="000250">*[DANDI:000250](https://dandiarchive.org/dandiset/000250/draft)*: **High-resolution tracking of Drosophila during egg-laying**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **3**, total size (MB): **100.32**

- Species: **Drosophila melanogaster - Fruit fly**

- Keywords: **Drosophila**, **egg laying**, **flies**, **decision making**, **behavioral sequence**

- Variables measured: **ProcessingModule**, **SpatialSeries**, **Position**

- Source paper: *Vijayan, Vikram; Maimon, Gaby (2023) High-resolution tracking of Drosophila during egg-laying*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000250_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 35.81 MB | 
[File info](https://api.dandiarchive.org/api/assets/029d73d2-e3d0-497f-92d5-1122327024d1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000250/draft/files?location=sub-CS-fly#-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/029d73d2-e3d0-497f-92d5-1122327024d1/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000251">*[DANDI:000251](https://dandiarchive.org/dandiset/000251/draft)*: **A Unified Framework for Dopamine Signals across Timescales**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **513**, total size (MB): **2,170.12**

- Species: **Mus musculus - House mouse**

- Variables measured: **SpatialSeries**, **ProcessingModule**, **Units**

- Source paper: *Kim, HyungGoo; Malik, Athar; Mikhael, John; Bech, Pol; Tsutsui-Kimura, Iku; Sun, Fangmiao; Zhang, Yajun; Li, Yulong; Watabe-Uchida, Mitsuko; Gershman, Samuel; Uchida, Naoshige (2023) A Unified Framework for Dopamine Signals across Timescales*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000251_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1.04 MB | 
[File info](https://api.dandiarchive.org/api/assets/df495f09-bd0e-4276-871e-51775cb57e43) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000251/draft/files?location=sub-3021%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/df495f09-bd0e-4276-871e-51775cb57e43/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 1.42 MB | 
[File info](https://api.dandiarchive.org/api/assets/b3327f7f-6e06-4dca-88c4-c489ee0fed74) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000251/draft/files?location=sub-3045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b3327f7f-6e06-4dca-88c4-c489ee0fed74/download/) 
---

<a id="000252">*[DANDI:000252](https://dandiarchive.org/dandiset/000252/draft)*: **Finger_RL: human intracortical recordings during attempted finger movements of right and left hands**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **12**, total size (MB): **38.13**

- Species: **Homo sapiens - Human**

- Keywords: **PPC**, **human**, **finger**, **MC**, **posterior parietal cortex**, **motor cortex**, **ipsilateral**

- Variables measured: **ElectrodeGroup**, **Units**

- Source paper: *Guan, Charles; Aflalo, Tyson; Kadlec, Kelly; Gamez, Jorge (2023) Finger_RL: human intracortical recordings during attempted finger movements of right and left hands*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000252_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1.52 MB | 
[File info](https://api.dandiarchive.org/api/assets/c9f1cd09-a210-413f-9c82-b43bdfdd19a3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000252/draft/files?location=sub-P1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c9f1cd09-a210-413f-9c82-b43bdfdd19a3/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 9.39 MB | 
[File info](https://api.dandiarchive.org/api/assets/d5bd9c5e-9410-4d58-8684-2c01b1a11b2a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000252/draft/files?location=sub-N1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d5bd9c5e-9410-4d58-8684-2c01b1a11b2a/download/) 
---

<a id="000255">*[DANDI:000255](https://dandiarchive.org/dandiset/000255/draft)*: **A unified 3D map of microscopic architecture and MRI of the human brain**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Bazin, Pierre-Louis (2022) A unified 3D map of microscopic architecture and MRI of the human brain*

---

<a id="000288">*[DANDI:000288](https://dandiarchive.org/dandiset/000288/draft)*: **20220630_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **36**, total size (MB): **1,049.74**

- Species: **Homo sapiens - Human**

- Keywords: **Patch-seq**, **human**

- Variables measured: **VoltageClampSeries**, **CurrentClampStimulusSeries**, **ProcessingModule**, **CurrentClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Mei, Nicholas; Chartrand, Thomas; Kalmbach, Brian; Molnar, Gabor; Tamas, Gabor; Lein, Ed (2023) 20220630_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000288_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 13.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/6ffde7c8-11de-44c7-a1fb-f8fff95cee14) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000288/draft/files?location=sub-H18.03.003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/6ffde7c8-11de-44c7-a1fb-f8fff95cee14/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 19.14 MB | 
[File info](https://api.dandiarchive.org/api/assets/f78bc98d-ca3a-4398-a60a-f579734de177) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000288/draft/files?location=sub-H19.03.316%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f78bc98d-ca3a-4398-a60a-f579734de177/download/) 
---

<a id="000290">*[DANDI:000290](https://dandiarchive.org/dandiset/000290/draft)*: **Diaz-Torga_Sfig1**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Abeledo Machado, Alejandra (2022) Diaz-Torga_Sfig1*

---

<a id="000292">*[DANDI:000292](https://dandiarchive.org/dandiset/000292/draft)*: **UHN whole-cell patch-clamp excitability recordings from mouse cortical neurons**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **11**, total size (MB): **13.76**

- Species: **Mus musculus - House mouse**

- Keywords: **excitability**, **cortex**, **mouse**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**

- Source paper: *Howard, Derek; Chameh, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell patch-clamp excitability recordings from mouse cortical neurons*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000292_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.94 MB | 
[File info](https://api.dandiarchive.org/api/assets/5eba84f6-1459-4833-9de2-102c65734e4e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000292/draft/files?location=sub-18208024%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/5eba84f6-1459-4833-9de2-102c65734e4e/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 1.04 MB | 
[File info](https://api.dandiarchive.org/api/assets/d98b0dcf-4299-4c06-8843-97750a12d53a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000292/draft/files?location=sub-2018-02-08-0001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d98b0dcf-4299-4c06-8843-97750a12d53a/download/) 
---

<a id="000293">*[DANDI:000293](https://dandiarchive.org/dandiset/000293/draft)*: **UHN whole-cell patch-clamp excitability recordings from human cortical neurons**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **121**, total size (MB): **234.98**

- Species: **Homo sapiens - Human**

- Keywords: **excitability**, **human**, **cortex**

- Variables measured: **VoltageClampStimulusSeries**, **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Howard, Derek; Moradi, Homeira Moradi; Valiante, Taufik; Tripathy, Shreejoy (2022) UHN whole-cell patch-clamp excitability recordings from human cortical neurons*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000293_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/497b0b7f-cf8e-48eb-b949-e730720568a3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000293/draft/files?location=sub-1914-2019-11-28-0038%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/497b0b7f-cf8e-48eb-b949-e730720568a3/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 0.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/e3024e2a-fd3e-447e-9caa-94470aeebc4a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000293/draft/files?location=sub-1911-19o10045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e3024e2a-fd3e-447e-9caa-94470aeebc4a/download/) 
---

<a id="000294">*[DANDI:000294](https://dandiarchive.org/dandiset/000294/draft)*: **A multi-modal fitting approach to construct single-neuron models with patch-clamp and high-density microelectrode arrays**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **2**, total size (MB): **18,173.61**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **HD-MEA, patch-clamp, multimodal**

- Variables measured: **ElectricalSeries**, **ProcessingModule**, **CurrentClampSeries**, **CurrentClampStimulusSeries**, **ElectrodeGroup**

- Source paper: *Buccino, Alessio Paolo; Damart, Tanguy; Bartram, Julian; Mandge, Darshan; Xue, Xiaohan; Zbili, Mickael; Gänswein, Tobias; Jaquier, Aurelien; Emmenegger, Vishalini; Markram, Henry; Hierlemann, Andreas; Van Geit, Werner (2023) A multi-modal fitting approach to construct single-neuron models with patch-clamp and high-density microelectrode arrays*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000295">*[DANDI:000295](https://dandiarchive.org/dandiset/000295/draft)*: **Electrophysiological properties of adult mouse spinal cord neurons - 22Q2_Ephys_DANDI**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **26**, total size (MB): **476.09**

- Species: **Mus musculus - House mouse**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**

- Source paper: *Zhang, Guang-Wei; Tao, Can (2022) Electrophysiological properties of adult mouse spinal cord neurons - 22Q2_Ephys_DANDI*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000295_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 9.15 MB | 
[File info](https://api.dandiarchive.org/api/assets/75fa33f2-c744-41ff-938b-c16bd345e39d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000295/draft/files?location=sub-20220701004%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/75fa33f2-c744-41ff-938b-c16bd345e39d/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 12.35 MB | 
[File info](https://api.dandiarchive.org/api/assets/5e43b224-33ff-4502-9291-d0a8b57579e1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000295/draft/files?location=sub-20220512002%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/5e43b224-33ff-4502-9291-d0a8b57579e1/download/) 
---

<a id="000296">*[DANDI:000296](https://dandiarchive.org/dandiset/000296/draft)*: **Drosophila visual neural responses to stochastic stimuli**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1278**, total size (MB): **745,311.36**

- Species: **Drosophila melanogaster - Fruit fly**

- Variables measured: **ImagingPlane**, **OpticalChannel**, **TwoPhotonSeries**

- Source paper: *Gonzalez, Aneysis (2022) Drosophila visual neural responses to stochastic stimuli*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000296_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 160.44 MB | 
[File info](https://api.dandiarchive.org/api/assets/8269630b-c5c9-4f6c-ba46-f69b007b998d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000296/draft/files?location=sub-3204989286909019890%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8269630b-c5c9-4f6c-ba46-f69b007b998d/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 170.79 MB | 
[File info](https://api.dandiarchive.org/api/assets/a6254199-b24a-4dca-9296-4ad1b2f94528) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000296/draft/files?location=sub-3342064158402930368%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a6254199-b24a-4dca-9296-4ad1b2f94528/download/) 
---

<a id="000297">*[DANDI:000297](https://dandiarchive.org/dandiset/000297/draft)*: **UHN whole-cell patch-clamp excitability recordings from human cortical neurons**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **118**, total size (MB): **231.1**

- Species: **Homo sapiens - Human**

- Keywords: **excitability**, **human**, **cortex**

- Variables measured: **CurrentClampSeries**, **VoltageClampStimulusSeries**, **CurrentClampStimulusSeries**

- Source paper: *Howard, Derek; Homeira Moradi, Chameh; Taufik A Valiante; Shreejoy Tripathy (2022) UHN whole-cell patch-clamp excitability recordings from human cortical neurons*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000297_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/0722fb00-ede2-4dcc-8f5d-005319c92e7e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000297/draft/files?location=sub-1914-2019-11-28-0038%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0722fb00-ede2-4dcc-8f5d-005319c92e7e/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 0.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/d2763c7d-a040-4c14-9327-fe8aca272a81) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000297/draft/files?location=sub-1911-19o10045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d2763c7d-a040-4c14-9327-fe8aca272a81/download/) 
---

<a id="000298">*[DANDI:000298](https://dandiarchive.org/dandiset/000298/draft)*: **Brain_stim_and_FSCV_and_ensemble_recording_anesthetized**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **FSCV, electrophysiology, brain stimulation**

- Source paper: *Cowen, Stephen (2022) Brain_stim_and_FSCV_and_ensemble_recording_anesthetized*

---

<a id="000299">*[DANDI:000299](https://dandiarchive.org/dandiset/000299/draft)*: **Stephen Test Set**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **1**, total size (MB): **0.23**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Cowen, Stephen (2022) Stephen Test Set*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000299_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.23 MB | 
[File info](https://api.dandiarchive.org/api/assets/12bb96be-3535-4144-82b5-4f23abe76b32) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000299/draft/files?location=sub-Rat203%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/12bb96be-3535-4144-82b5-4f23abe76b32/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000301">*[DANDI:000301](https://dandiarchive.org/dandiset/000301/draft)*: **Extracellular electrophysiology unit data from mouse Superior Colliculus during whisker guided virtual navigation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **14**, total size (MB): **29,683.19**

- Species: **Mus musculus - House mouse**

- Variables measured: **SpatialSeries**, **ProcessingModule**, **Units**, **ElectrodeGroup**, **Position**

- Source paper: *Chinta, Suma; Pluta, Scott (2023) Extracellular electrophysiology unit data from mouse Superior Colliculus during whisker guided virtual navigation*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000301_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1356.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/3fc83f98-5c71-4891-b5a2-4b00760402e4) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000301/draft/files?location=sub-M26%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3fc83f98-5c71-4891-b5a2-4b00760402e4/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 1920.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/d2a9c61e-ec6a-4d37-8d93-70ff23b37a6d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000301/draft/files?location=sub-M43%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d2a9c61e-ec6a-4d37-8d93-70ff23b37a6d/download/) 
---

<a id="000302">*[DANDI:000302](https://dandiarchive.org/dandiset/000302/draft)*: **Habenular neurophysiology**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **32**, total size (MB): **1,078.71**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralEvents**, **ProcessingModule**, **Units**, **ElectrodeGroup**, **OptogeneticSeries**

- Source paper: *Jo, YoungJu (2023) Habenular neurophysiology*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000302_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 10.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/6f12e5fb-f864-4349-a31b-3d5a258acada) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000302/draft/files?location=sub-ANM-0172%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/6f12e5fb-f864-4349-a31b-3d5a258acada/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 12.43 MB | 
[File info](https://api.dandiarchive.org/api/assets/8fb0ec6c-bf5a-446f-b2bb-9bdf30b21f2e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000302/draft/files?location=sub-ANM-0174%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8fb0ec6c-bf5a-446f-b2bb-9bdf30b21f2e/download/) 
---

<a id="000335">*[DANDI:000335](https://dandiarchive.org/dandiset/000335/draft)*: **My Test Dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Neufeld, Shay (2022) My Test Dataset*

---

<a id="000337">*[DANDI:000337](https://dandiarchive.org/dandiset/000337/draft)*: **20220917_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **21**, total size (MB): **1,532.06**

- Species: **Homo sapiens - Human**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Chartrand, Thomas (2022) 20220917_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000337_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 27.46 MB | 
[File info](https://api.dandiarchive.org/api/assets/44998ede-ef66-4017-bb7c-8be8a77bfba8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000337/draft/files?location=sub-1089233462%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/44998ede-ef66-4017-bb7c-8be8a77bfba8/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 29.8 MB | 
[File info](https://api.dandiarchive.org/api/assets/5e32b8af-e756-406f-a195-67889b611fe3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000337/draft/files?location=sub-701201569%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/5e32b8af-e756-406f-a195-67889b611fe3/download/) 
---

<a id="000338">*[DANDI:000338](https://dandiarchive.org/dandiset/000338/draft)*: **groupweight BMI**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **2**, total size (MB): **740.23**

- Species: **Macaca mulatta - Rhesus monkey**

- Keywords: **BCI BMI **

- Variables measured: 

- Source paper: *Zhang, Chenguang (2022) groupweight BMI*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000338_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 418.92 MB | 
[File info](https://api.dandiarchive.org/api/assets/721133ab-a29b-4533-9fc8-823e290e7d84) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000338/draft/files?location=sub-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/721133ab-a29b-4533-9fc8-823e290e7d84/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000339">*[DANDI:000339](https://dandiarchive.org/dandiset/000339/draft)*: **Local Field Potential Recordings in the Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **66**, total size (MB): **64,243.85**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **Ultrasound**, **tFUS**, **Plasticity**, **Somatosensory**, **Rat**, **Somatosensory Cortex**

- Variables measured: **ProcessingModule**, **ElectricalSeries**, **LFP**, **ElectrodeGroup**

- Source paper: *Ramachandran, Sandhya; Carnegie Mellon University; Niu, Xiaodan; Yu, Kai; He, Bin (2023) Local Field Potential Recordings in the Primary Somatosensory Cortex before and after Transcranial Focused Ultrasound Stimulation in Rats*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000339_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 702.78 MB | 
[File info](https://api.dandiarchive.org/api/assets/f4a055e5-6fcd-4390-a3f0-52d6d44be2a2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000339/draft/files?location=sub-BH275%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f4a055e5-6fcd-4390-a3f0-52d6d44be2a2/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 703.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/eaf70c0d-f3f2-465a-9fda-783a24abc4c3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000339/draft/files?location=sub-BH266%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/eaf70c0d-f3f2-465a-9fda-783a24abc4c3/download/) 
---

<a id="000340">*[DANDI:000340](https://dandiarchive.org/dandiset/000340/draft)*: **Allen Institute Openscope - Credit Assignment project with stimuli templates**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Lecoq, Jerome (2022) Allen Institute Openscope - Credit Assignment project with stimuli templates*

---

<a id="000341">*[DANDI:000341](https://dandiarchive.org/dandiset/000341/draft)*: **Temporal disparity of action potentials triggered in axon initial segments and distal axons in the neocortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **787**, total size (MB): **711,580.68**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **Layer 1 interneurons**, **human**, **rodent**, **in vitro**, **in vivo**, **Retroaxonal firing**, **Persistent firing**, **Retoaxonal action potentials**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Tóth, Martin; Rózsa, Márton (2023) Temporal disparity of action potentials triggered in axon initial segments and distal axons in the neocortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000341_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 13.05 MB | 
[File info](https://api.dandiarchive.org/api/assets/ffe2911b-f8a4-48ea-98be-8b2910719c50) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000341/draft/files?location=sub-1809131og%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ffe2911b-f8a4-48ea-98be-8b2910719c50/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 16.42 MB | 
[File info](https://api.dandiarchive.org/api/assets/dd31e463-89d3-4531-850a-c2dfd4e12e4d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000341/draft/files?location=sub-20120627%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/dd31e463-89d3-4531-850a-c2dfd4e12e4d/download/) 
---

<a id="000343">*[DANDI:000343](https://dandiarchive.org/dandiset/000343/draft)*: **da_network_2022**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Miller, Douglas (2022) da_network_2022*

---

<a id="000346">*[DANDI:000346](https://dandiarchive.org/dandiset/000346/draft)*: **Test dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Griggs, Whitney (2022) Test dataset*

---

<a id="000347">*[DANDI:000347](https://dandiarchive.org/dandiset/000347/draft)*: **Multiphoton imaging in macaque visual cortex (preliminary data)**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **9**, total size (MB): **26,039.39**

- Species: **Macaca nemestrina - Pig-tailed macaque**

- Variables measured: **OpticalChannel**, **PlaneSegmentation**, **ImagingPlane**, **TwoPhotonSeries**, **ProcessingModule**

- Source paper: *Chatterjee, Soumya (2022) Multiphoton imaging in macaque visual cortex (preliminary data)*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000348">*[DANDI:000348](https://dandiarchive.org/dandiset/000348/draft)*: **Tanabe-2022-CurrentBiology**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Cang, JC (2022) Tanabe-2022-CurrentBiology*

---

<a id="000349">*[DANDI:000349](https://dandiarchive.org/dandiset/000349/draft)*: **HMV-test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Martínez Vergara, Hernando (2022) HMV-test*

---

<a id="000350">*[DANDI:000350](https://dandiarchive.org/dandiset/000350/draft)*: **Glia Accumulate Evidence that Actions Are Futile and Suppress Unsuccessful Behavior**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **12**, total size (MB): **5,865,794.2**

- Species: **Danio rerio - Zebra fish**

- Keywords: **neuroscience**, **glia**, **astrocytes**, **norepinephrine**, **noradrenaline**, **learned helplessness**, **neuromodulation**, **behavioral states**, **evidence accumulation**, **zebrafish**

- Variables measured: **TwoPhotonSeries**, **OpticalChannel**, **ProcessingModule**, **ImagingPlane**, **PlaneSegmentation**

- Source paper: *Mu, Yu; Bennett, Davis V.; Rubinov, Mikail; Lim, Jing-Xuan; Yang, Chao-Tsung; Tanimoto, Masashi; Mensh, Brett D. ; Looger, Loren L.; Narayan, Sujatha; Ahrens, Misha B. (2023) Glia Accumulate Evidence that Actions Are Futile and Suppress Unsuccessful Behavior*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000351">*[DANDI:000351](https://dandiarchive.org/dandiset/000351/draft)*: **Jeong et al (2022) Mesolimbic dopamine release conveys causal associations**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.4.0**), file count: **428**, total size (MB): **98,548.17**

- Species: **Mus musculus - House mouse**

- Variables measured: **ProcessingModule**

- Source paper: *Jeong, Huijeong; Taylor, Annie; Floeder, Joseph R ; Lohmann, Martin; Mihalas, Stefan; Wu, Brenda; Zhou, Mingkang; Burke, Dennis A; K Namboodiri, Vijay Mohan (2022) Jeong et al (2022) Mesolimbic dopamine release conveys causal associations*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000351_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/1cbaaedf-d013-4366-b099-878566b003c9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000351/draft/files?location=sub-DB-longITI-C1-M1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1cbaaedf-d013-4366-b099-878566b003c9/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.22 MB | 
[File info](https://api.dandiarchive.org/api/assets/fbd6d414-ece1-4f50-b653-a55ec99f24b8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000351/draft/files?location=sub-DB-longITI-C1-M2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/fbd6d414-ece1-4f50-b653-a55ec99f24b8/download/) 
---

<a id="000359">*[DANDI:000359](https://dandiarchive.org/dandiset/000359/draft)*: **Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Paulk, Angelique C (2022) Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics*

---

<a id="000362">*[DANDI:000362](https://dandiarchive.org/dandiset/000362/draft)*: **Simultaneous loose seal cell-attached recordings and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli  - RAW movies**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **52**, total size (MB): **397,456.46**

- Species: **Mus musculus - House mouse**

- Variables measured: **ProcessingModule**, **OpticalChannel**, **ImagingPlane**, **TwoPhotonSeries**, **PlaneSegmentation**, **CurrentClampStimulusSeries**, **CurrentClampSeries**, **VoltageClampSeries**, **VoltageClampStimulusSeries**

- Source paper: *Rózsa, Márton (2022) Simultaneous loose seal cell-attached recordings and two-photon imaging of GCaMP8 expressing mouse V1 neurons with drifting gratings visual stimuli  - RAW movies*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000363">*[DANDI:000363](https://dandiarchive.org/dandiset/000363/draft)*: **Mesoscale Activity Map Dataset**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **174**, total size (MB): **65,700,262.85**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralTimeSeries**, **BehavioralEvents**, **ElectrodeGroup**, **Units**, **ElectricalSeries**

- Source paper: *Chen, Susu; Nguyen, Thinh; Li, Nuo; Svoboda, Karel (2023) Mesoscale Activity Map Dataset*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000363_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 159.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/445029d5-0023-4915-9d7d-25eb11451adc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000363/draft/files?location=sub-440958%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/445029d5-0023-4915-9d7d-25eb11451adc/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 171.34 MB | 
[File info](https://api.dandiarchive.org/api/assets/2953ce80-883a-48b6-9750-c6de9d0028a5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000363/draft/files?location=sub-442571%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2953ce80-883a-48b6-9750-c6de9d0028a5/download/) 
---

<a id="000364">*[DANDI:000364](https://dandiarchive.org/dandiset/000364/draft)*: **M1_waterGrab**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhu, Feng (2022) M1_waterGrab*

---

<a id="000397">*[DANDI:000397](https://dandiarchive.org/dandiset/000397/draft)*: **Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **3**, total size (MB): **24,071.28**

- Species: **Homo sapiens - Human**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Paulk, Angelique C; Kfir, Yoav; Khanna, Arjun R; Mustroph, Martina L; Trautmann, Eric M; Soper, Dan J; Stavisky, Sergey D; Welkenhuysen, Marleen; Dutta, Barundeb; Shenoy, Krisha V; Hochberg, Leigh R; Richardson, R. Mark; Williams, Ziv M; Cash, Sydney S (2022) Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000398">*[DANDI:000398](https://dandiarchive.org/dandiset/000398/draft)*: **Scalable Thousand Channel Penetrating Microneedle Arrays on Flex for Multimodal and Large Area Coverage BrainMachine Interfaces**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **42**, total size (MB): **61,125.8**

- Species: **Mus musculus - House mouse**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Lee, Sang Heon; Thunemann, Martin; Lee, Keundong; Cleary, Daniel R.; Tonsfeldt, Karen J.; Oh, Hongseok; Azzazy, Farid; Tchoe, Youngbin; Bourhis, Andrew M.; Hossain, Lorraine; Ro, Yun Goo; Tanaka, Atsunori; Kılıç, Kıvılcım ; Devor, Anna; Dayeh, Shadi A. (2022) Scalable Thousand Channel Penetrating Microneedle Arrays on Flex for Multimodal and Large Area Coverage BrainMachine Interfaces*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000398_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 106.35 MB | 
[File info](https://api.dandiarchive.org/api/assets/591a4423-cc24-40c6-966e-20d782d68a53) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000398/draft/files?location=sub-San2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/591a4423-cc24-40c6-966e-20d782d68a53/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 113.04 MB | 
[File info](https://api.dandiarchive.org/api/assets/5b5adae9-82e0-44aa-9faa-c827351d117a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000398/draft/files?location=sub-San4%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/5b5adae9-82e0-44aa-9faa-c827351d117a/download/) 
---

<a id="000399">*[DANDI:000399](https://dandiarchive.org/dandiset/000399/draft)*: **All-optical physiology resolves a synaptic basis for behavioral time scale plasticity**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **105**, total size (MB): **86.58**

- Species: **Mus musculus - House mouse**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Fan, Linlin (2023) All-optical physiology resolves a synaptic basis for behavioral time scale plasticity*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000399_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.46 MB | 
[File info](https://api.dandiarchive.org/api/assets/14df4c07-159e-471c-afae-7af889d01539) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000399/draft/files?location=sub-1-7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/14df4c07-159e-471c-afae-7af889d01539/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 0.51 MB | 
[File info](https://api.dandiarchive.org/api/assets/608a8f55-7628-4d7f-ad0e-8515cd05bd7f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000399/draft/files?location=sub-19%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/608a8f55-7628-4d7f-ad0e-8515cd05bd7f/download/) 
---

<a id="000400">*[DANDI:000400](https://dandiarchive.org/dandiset/000400/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Macdonald, Austin (2022) test*

---

<a id="000401">*[DANDI:000401](https://dandiarchive.org/dandiset/000401/draft)*: **touchExploration: human S1 recordings with multisensory tactile stimuli in arm and finger**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Rosenthal, Isabelle (2022) touchExploration: human S1 recordings with multisensory tactile stimuli in arm and finger*

---

<a id="000402">*[DANDI:000402](https://dandiarchive.org/dandiset/000402/draft)*: **MICrONS Two Photon Functional Imaging**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **19**, total size (MB): **1,347,665.45**

- Species: **Mus musculus - House mouse**

- Variables measured: **SpatialSeries**, **ImagingPlane**, **OpticalChannel**, **EyeTracking**, **PupilTracking**, **PlaneSegmentation**, **ProcessingModule**, **TwoPhotonSeries**

- Source paper: *Bae, J. Alexander; Baptiste, Mahaly; Bodor, Agnes L.; Brittain, Derrick; Buchanan, JoAnn; Bumbarger, Daniel J.; Castro, Manuel A.; Celii, Brendan; Cobos, Erick ; Collman, Forrest; Maçarico da Costa, Nuno; Dorkenwald, Sven; Elabbady, Leila; Fahey, Paul G.; Fliss, Tim; Gager, Jay; Gamlin, Clare; Halageri, Akhilesh; Hebditch, James; Jia, Zhen; Jordan, Chris; Kapner, Daniel; Kemnitz, Nico; Kinn, Sam; Koolman, Selden; Kuehner, Kai; Lee, Kisuk; Li, Kai; Lu, Ran; Macrina, Thomas; Mahalingam, Gayathri; McReynolds, Sarah; Miranda, Elanine; Mitchell, Eric; Mondal, Shanka Subhra; Moore, Merlin; Mu, Shang; Muhammad, Taliah; Nehoran, Barak; Ogedengbe, Oluwaseun; Papadopoulos, Christos; Papadopoulos, Stelios; Patel, Saumil; Pitkow, Xaq; Popovych, Sergiy; Ramos, Anthony; Reid, R. Clay; Reimer, Jacob; Schneider-Mizell, Casey M.; Seung, H. Sebastian; Silverman, Ben; Silversmith, William; Sterling, Amy; Sinz, Fabian H.; Smith, Cameron L.; Suckow, Shelby; Takeno, Marc; Tan, Zheng H.; Tolias, Andreas S.; Torres, Russel; Turner, Nicholas L.; Walker, Edgar Y.; Wang, Tianyu; Williams, Grace; Williams, Sarah; Willie, Kyle; Willie, Ryan; Wong, William; Wu, Jingpeng; Xu, Chris; Yang, Runzhe; Yatsenko, Dimitri; Ye, Fei; Yin, Wenjing; Yu, Szi-chieh (2023) MICrONS Two Photon Functional Imaging*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000404">*[DANDI:000404](https://dandiarchive.org/dandiset/000404/draft)*: **Monkey 2D cursor BMI**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **13**, total size (MB): **1,046.74**

- Species: **Macaca mulatta - Rhesus monkey**

- Keywords: **neural population dynamics**, **motor cortex**, **motor control**, **brain-machine interface**, **neuroprosthetics**, **optimal feedback control**, **motor commands**, **movement representations**, **dynamical systems **

- Variables measured: **ProcessingModule**

- Source paper: *Athalye, Vivek R; Khanna, Preeya; Gowda, Suraj; Orsborn, Amy L; Costa, Rui M; Carmena, Jose M (2023) Monkey 2D cursor BMI*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000404_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 18.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/53815e58-0703-4912-ac72-4244bd4a85b0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000404/draft/files?location=sub-monk-g%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/53815e58-0703-4912-ac72-4244bd4a85b0/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 71.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/fc69022c-ccdc-49ef-a5bb-662f3cb87ee0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000404/draft/files?location=sub-monk-j%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/fc69022c-ccdc-49ef-a5bb-662f3cb87ee0/download/) 
---

<a id="000405">*[DANDI:000405](https://dandiarchive.org/dandiset/000405/draft)*: **Gonzalez & Giocomo (2022) Parahippocampal neurons encode task-relevant information for goal-directed navigation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **276**, total size (MB): **3,877.49**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: 

- Source paper: *Gonzalez, Alex (2023) Gonzalez & Giocomo (2022) Parahippocampal neurons encode task-relevant information for goal-directed navigation*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000405_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/40fc445d-7fc8-4de4-81f2-1ccee6d97347) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000405/draft/files?location=sub-s2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/40fc445d-7fc8-4de4-81f2-1ccee6d97347/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 1.64 MB | 
[File info](https://api.dandiarchive.org/api/assets/b7d4e75e-5477-4d53-a4b0-1688fd0f1260) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000405/draft/files?location=sub-s4%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b7d4e75e-5477-4d53-a4b0-1688fd0f1260/download/) 
---

<a id="000406">*[DANDI:000406](https://dandiarchive.org/dandiset/000406/draft)*: **Spyglass sample data**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **spyglass**

- Source paper: *Adenekan, Phil (2023) Spyglass sample data*

---

<a id="000409">*[DANDI:000409](https://dandiarchive.org/dandiset/000409/draft)*: **IBL - Brain Wide Map**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **1582**, total size (MB): **34,256,200.51**

- Species: **Mus musculus - House mouse**

- Keywords: **International Brain Laboratory**, **multi-probe**, **Neuropixels**, **Allen Mouse Brain CCFv3**, **Allen Mouse Brain Atlas**, **head-fixed**, **decision-making**, **face-tracking**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**, **CompassDirection**, **Units**, **SpatialSeries**, **PupilTracking**, **ProcessingModule**

- Source paper: *International Brain Laboratory; Benson, Brandon; Benson, Julius; Birman, Daniel; Bonacchi, Niccolò; Carandini, Matteo; Catarino, Joana; Chapuis, Gaelle; Dayan, Peter; DeWitt, Eric; Engel, Tatiana; Fabbri, Michele; Faulkner, Mayo; Fiete, Ila; Findling, Charles; Freitas-Silva, Laura; Gerçek, Berk; Harris, Kenneth; Hofer, Sonja; Hu, Fei; Hubert, Félix; Huntenburg, Julia; Khanal, Anup; Langdon, Christopher; Lau, Petrina; Meijer, Guido; Miska, Nathaniel; Noel, Jean-Paul; Nylund, Kai; Pan-Vazquez, Alejandro; Pouget, Alexandre; Rossant, Cyrille; Roth, Noam; Schaeffer, Rylan; Schartner, Michael; Shi, Yanliang; Socha, Karolina; Steinmetz, Nicholas; Svoboda, Karel; Urai, Anne; Wells, Miles; West, Steven; Whiteway, Mathew; Winter, Olivier; Witten, Ilana (2023) IBL - Brain Wide Map*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000409_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 124.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/37a85ccc-1bc2-4c5e-aa87-2b2ecaacf71f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000409/draft/files?location=sub-ibl-witten-19%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/37a85ccc-1bc2-4c5e-aa87-2b2ecaacf71f/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 131.91 MB | 
[File info](https://api.dandiarchive.org/api/assets/8098c7a7-9a4e-4ff4-94a0-5a46d499fb75) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000409/draft/files?location=sub-ibl-witten-17%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8098c7a7-9a4e-4ff4-94a0-5a46d499fb75/download/) 
---

<a id="000410">*[DANDI:000410](https://dandiarchive.org/dandiset/000410/draft)*: **Joshi et al (2023) Dynamic Synchronization between Hippocampal Spatial Representations and the Stepping Rhythm**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **22**, total size (MB): **2,802,041.98**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **SpatialSeries**, **ProcessingModule**, **Position**, **BehavioralEvents**, **ElectricalSeries**

- Source paper: *Joshi, Abhilasha (2023) Joshi et al (2023) Dynamic Synchronization between Hippocampal Spatial Representations and the Stepping Rhythm*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000411">*[DANDI:000411](https://dandiarchive.org/dandiset/000411/draft)*: **test**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **1**, total size (MB): **0.23**

- Species: **Mus musculus - House mouse**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Li, Chenyang (2023) test*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000411_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.23 MB | 
[File info](https://api.dandiarchive.org/api/assets/c3d0b58d-e5d8-4913-92fd-dc98927ce696) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000411/draft/files?location=sub-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c3d0b58d-e5d8-4913-92fd-dc98927ce696/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000444">*[DANDI:000444](https://dandiarchive.org/dandiset/000444/draft)*: **Dynamic corticothalamic gain modulation of the somatosensory thalamocortical circuit during wakefulness**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **mouse**, **cortex**, ** thalamus**, **corticothalamic feedback**, **sensory processing**, **somatosensation**

- Source paper: *Dimwamwa, Elaida; Stanley, Garrett (2023) Dynamic corticothalamic gain modulation of the somatosensory thalamocortical circuit during wakefulness*

---

<a id="000445">*[DANDI:000445](https://dandiarchive.org/dandiset/000445/draft)*: **EDTest**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Dimwamwa, Elaida (2023) EDTest*

---

<a id="000446">*[DANDI:000446](https://dandiarchive.org/dandiset/000446/draft)*: **Test upload**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Brooks, Frederick (2023) Test upload*

---

<a id="000447">*[DANDI:000447](https://dandiarchive.org/dandiset/000447/draft)*: **Novel-familiar-novel WTrack (CA1-PFC)**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **5**, total size (MB): **35,480.04**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **Hippocampus, Prefrontal cortex, Learning, Memory, Decision making**

- Variables measured: **Position**, **ElectricalSeries**, **Units**, **ElectrodeGroup**, **LFP**, **ProcessingModule**, **SpatialSeries**

- Source paper: *Shin, Justin; Jadhav, Shantanu P (2023) Novel-familiar-novel WTrack (CA1-PFC)*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000448">*[DANDI:000448](https://dandiarchive.org/dandiset/000448/draft)*: **Time kinetics of the membrane potential at the cathode- and anode-facing poles of a cell induced by a train of 5 pulses at 833 kHz**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **18**, total size (MB): **3,173.07**

- Species: **Cricetulus griseus - Cricetulus aureus**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) Time kinetics of the membrane potential at the cathode- and anode-facing poles of a cell induced by a train of 5 pulses at 833 kHz*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000448_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 173.64 MB | 
[File info](https://api.dandiarchive.org/api/assets/50f1e8fa-f1c3-48d9-9f62-3fe536daa49e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000448/draft/files?location=sub-007-F%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/50f1e8fa-f1c3-48d9-9f62-3fe536daa49e/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 174.49 MB | 
[File info](https://api.dandiarchive.org/api/assets/00b115be-670d-4ee8-b2bb-8fa65aaea6ec) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000448/draft/files?location=sub-009-F%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/00b115be-670d-4ee8-b2bb-8fa65aaea6ec/download/) 
---

<a id="000449">*[DANDI:000449](https://dandiarchive.org/dandiset/000449/draft)*: **Moving_C_Elegans_Corrected_Voleti_2019**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Simko, Peter (2023) Moving_C_Elegans_Corrected_Voleti_2019*

---

<a id="000451">*[DANDI:000451](https://dandiarchive.org/dandiset/000451/draft)*: **Single Day WTrack Learning**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Shin, Justin (2023) Single Day WTrack Learning*

---

<a id="000452">*[DANDI:000452](https://dandiarchive.org/dandiset/000452/draft)*: **Parabrachial**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Keller, Asaf (2023) Parabrachial*

---

<a id="000454">*[DANDI:000454](https://dandiarchive.org/dandiset/000454/draft)*: **Guide to the construction and use of an adaptive optics two-photon microscope with direct wavefront sensing**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **4**, total size (MB): **7,401.24**

- Species: **Mus musculus - House mouse**

- Variables measured: **TwoPhotonSeries**, **ImagingPlane**, **OpticalChannel**

- Source paper: *Klienfeld, David; Yao, Pantong; Liu, Rui; Broginni, Thomas; Thunemann, Martin; University of California, San Diego; Boston University; University of California, San Diego (2023) Guide to the construction and use of an adaptive optics two-photon microscope with direct wavefront sensing*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000454_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 352.52 MB | 
[File info](https://api.dandiarchive.org/api/assets/ffc82542-17e0-4559-a253-a3fb07205485) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000454/draft/files?location=sub-rbp4-jRGECO1a-21%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ffc82542-17e0-4559-a253-a3fb07205485/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 3408.07 MB | 
[File info](https://api.dandiarchive.org/api/assets/b4bdca75-6b2d-460a-b616-175ef3ed2cf3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000454/draft/files?location=sub-SST-tdTomato-1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b4bdca75-6b2d-460a-b616-175ef3ed2cf3/download/) 
---

<a id="000455">*[DANDI:000455](https://dandiarchive.org/dandiset/000455/draft)*: **Coregistration of heading to visual cues in retrosplenial cortex**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Sit, Kevin (2023) Coregistration of heading to visual cues in retrosplenial cortex*

---

<a id="000456">*[DANDI:000456](https://dandiarchive.org/dandiset/000456/draft)*: **Accelerated signal propagation speed in human neocortical microcircuits**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Lákovics, Rajmund (2023) Accelerated signal propagation speed in human neocortical microcircuits*

---

<a id="000457">*[DANDI:000457](https://dandiarchive.org/dandiset/000457/draft)*: **Novel-familiar-novel WTrack (CA1-PFC)**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Shin, Justin (2023) Novel-familiar-novel WTrack (CA1-PFC)*

---

<a id="000458">*[DANDI:000458](https://dandiarchive.org/dandiset/000458/draft)*: **Simultaneous electroencephalography, extracellular electrophysiology, and cortical electrical stimulation in head-fixed mice**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **24**, total size (MB): **361,482.31**

- Species: **Mus musculus - House mouse**

- Keywords: **EEG**, **Neuropixels**, **electrical stimulation**, **brain states**, **cortico-thalamic interactions**, **extracellular electrophysiology**

- Variables measured: **BehavioralTimeSeries**, **Units**, **ElectricalSeries**, **ElectrodeGroup**, **LFP**, **ProcessingModule**

- Source paper: *Claar, Leslie D; Rembado, Irene; Kuyat, Jacqulyn R; Russo, Simone; Marks, Lydia C; Olsen, Shawn R; Koch, Christof (2023) Simultaneous electroencephalography, extracellular electrophysiology, and cortical electrical stimulation in head-fixed mice*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000458_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 428.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/ec27a42e-098f-418e-b5e6-1424d5bbdb90) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000458/draft/files?location=sub-521887%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ec27a42e-098f-418e-b5e6-1424d5bbdb90/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 504.31 MB | 
[File info](https://api.dandiarchive.org/api/assets/d77558e6-1b16-49c2-9f61-885d63701331) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000458/draft/files?location=sub-521886%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d77558e6-1b16-49c2-9f61-885d63701331/download/) 
---

<a id="000461">*[DANDI:000461](https://dandiarchive.org/dandiset/000461/draft)*: **Cohen Tickertapes Exploratory Data 1**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **14**, total size (MB): **23.37**

- Species: **Canis lupus familiaris - Dog**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **TwoPhotonSeries**

- Source paper: *Davis Ozawa, Hunter; National Institutes of Health (2023) Cohen Tickertapes Exploratory Data 1*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000461_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1.33 MB | 
[File info](https://api.dandiarchive.org/api/assets/764320de-4730-4897-b353-a5fdefbdc860) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000461/draft/files?location=sub-005%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/764320de-4730-4897-b353-a5fdefbdc860/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1.33 MB | 
[File info](https://api.dandiarchive.org/api/assets/2fabf7bb-da97-46a1-a4f3-45df19466e73) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000461/draft/files?location=sub-003%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2fabf7bb-da97-46a1-a4f3-45df19466e73/download/) 
---

<a id="000462">*[DANDI:000462](https://dandiarchive.org/dandiset/000462/draft)*: **HippocampusRewardDataset**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **14**, total size (MB): **6,494.59**

- Species: **Mus musculus - House mouse**

- Keywords: **hippocampus; dopamine; mice; reward; calcium imaging; VR based navigation; DREADD**

- Variables measured: **ProcessingModule**, **OpticalChannel**, **ImagingPlane**

- Source paper: *Krishnan, Seetha (2023) HippocampusRewardDataset*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000462_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 193.96 MB | 
[File info](https://api.dandiarchive.org/api/assets/f7d5fa97-49ab-4f68-b2c0-326e57c22dd4) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000462/draft/files?location=sub-NR6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f7d5fa97-49ab-4f68-b2c0-326e57c22dd4/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 221.95 MB | 
[File info](https://api.dandiarchive.org/api/assets/8fe4507e-2257-4604-abab-a2c2c8519192) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000462/draft/files?location=sub-NR32%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8fe4507e-2257-4604-abab-a2c2c8519192/download/) 
---

<a id="000463">*[DANDI:000463](https://dandiarchive.org/dandiset/000463/draft)*: **Electrophysiological Recordings in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **29**, total size (MB): **64,199.97**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ElectrodeGroup**, **LFP**, **ElectricalSeries**, **ProcessingModule**

- Source paper: *Ramachandran, Sandhya; He, Bin; Yu, Kai; Gao, Huan (2023) Electrophysiological Recordings in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000463_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1067.46 MB | 
[File info](https://api.dandiarchive.org/api/assets/b4f4fc91-51e5-41e9-9a0a-130df842f3dd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000463/draft/files?location=sub-BH396%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b4f4fc91-51e5-41e9-9a0a-130df842f3dd/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
   Size: 1839.54 MB | 
[File info](https://api.dandiarchive.org/api/assets/2e6b590a-a2a4-4455-bb9b-45cc3d7d7cc0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000463/draft/files?location=sub-BH395%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2e6b590a-a2a4-4455-bb9b-45cc3d7d7cc0/download/) 
---

<a id="000465">*[DANDI:000465](https://dandiarchive.org/dandiset/000465/draft)*: **Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **36**, total size (MB): **129,066.8**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **micro-ECoG, barrel cortex, high gamma activity**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Tchoe, Youngbin (2023) Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000466">*[DANDI:000466](https://dandiarchive.org/dandiset/000466/draft)*: **Optical Recording Exploratory Data 1**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Cubukcu, Ertugrul (2023) Optical Recording Exploratory Data 1*

---

<a id="000467">*[DANDI:000467](https://dandiarchive.org/dandiset/000467/draft)*: **Sparse and stereotyped encoding implicates a core glomerulus for ant alarm behavior**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **14685**, total size (MB): **1,262,490.25**

- Species: **Ooceraea biroi - Clonal raider ant**

- Keywords: **antennal lobe; calcium imaging; chemosensation; clonal raider ant; communication; GCaMP; odor coding; olfaction; Ooceraea biroi; pheromone**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **TwoPhotonSeries**

- Source paper: *Sparse and stereotyped encoding implicates a core glomerulus for ant alarm behavior (2023).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000467_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 84.09 MB | 
[File info](https://api.dandiarchive.org/api/assets/0ac27aba-b8a8-41e4-841b-4cfce7f26ea4) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000467/draft/files?location=sub-ant3-m4-d26-y2022%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0ac27aba-b8a8-41e4-841b-4cfce7f26ea4/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 84.09 MB | 
[File info](https://api.dandiarchive.org/api/assets/4f1d1f8e-c557-4f21-8913-581d1eca9089) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000467/draft/files?location=sub-ant3-m4-d21-y2022%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4f1d1f8e-c557-4f21-8913-581d1eca9089/download/) 
---

<a id="000468">*[DANDI:000468](https://dandiarchive.org/dandiset/000468/draft)*: **Human single-neuron activity during the Treasure Hunt spatial navigation task**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Donoghue, Thomas (2023) Human single-neuron activity during the Treasure Hunt spatial navigation task*

---

<a id="000469">*[DANDI:000469](https://dandiarchive.org/dandiset/000469/draft)*: **Dataset of human-single neuron activity during a Sternberg working memory task.**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **41**, total size (MB): **9,788.56**

- Species: **Homo sapiens - Human**

- Keywords: **cognitive neuroscience**, **data standardization**, **working memory**, **neurophysiology**, **neurosurgery**, **NWB**, **open source**, **single-neurons**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Kyzar, Michael; Kaminski, Jan; Brzezicka, Aneta; Reed, Chrystal M.; Chung, Jeffrey M. ; Mamelak, Adam M.; Rutishauser, Ueli (2024) Dataset of human-single neuron activity during a Sternberg working memory task*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000469_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 27.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/d452ea33-5135-47f8-9448-f6293e8fbea7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000469/draft/files?location=sub-19%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d452ea33-5135-47f8-9448-f6293e8fbea7/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 33.15 MB | 
[File info](https://api.dandiarchive.org/api/assets/d1970c9a-628e-4880-a67c-9c70108456ab) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000469/draft/files?location=sub-20%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d1970c9a-628e-4880-a67c-9c70108456ab/download/) 
---

<a id="000470">*[DANDI:000470](https://dandiarchive.org/dandiset/000470/draft)*: **Test**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **1**, total size (MB): **128.2**

- Species: **Mus musculus - House mouse**

- Variables measured: **ImagingPlane**, **ProcessingModule**, **OpticalChannel**

- Source paper: *Krishnan, Seetha (2023) Test*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000470_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 128.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/e2448bb8-9c73-49f8-a033-7d456dba83b2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000470/draft/files?location=sub-NR6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e2448bb8-9c73-49f8-a033-7d456dba83b2/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000472">*[DANDI:000472](https://dandiarchive.org/dandiset/000472/draft)*: **NeuroPAL volumetric images**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **18**, total size (MB): **3,880.85**

- Species: **Caenorhabditis elegans**

- Variables measured: **ProcessingModule**, **PlaneSegmentation**

- Source paper: *Sprague, Daniel (2023) NeuroPAL volumetric images*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000472_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-0**  
   Size: 197.07 MB | 
[File info](https://api.dandiarchive.org/api/assets/76a095cd-2bcf-401f-ab25-db25bcb22944) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000472/draft/files?location=sub-2021-12-03-w00-NP1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/76a095cd-2bcf-401f-ab25-db25bcb22944/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-0**  
   Size: 197.07 MB | 
[File info](https://api.dandiarchive.org/api/assets/c261a889-4cd3-4c31-bdfe-c9c5750a3a0a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000472/draft/files?location=sub-2022-01-22-w04-NP1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c261a889-4cd3-4c31-bdfe-c9c5750a3a0a/download/) 
---

<a id="000473">*[DANDI:000473](https://dandiarchive.org/dandiset/000473/draft)*: **Esr1+ hypothalamic-habenula neurons shape aversive states.**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **25**, total size (MB): **113,558.68**

- Species: **Mus musculus - House mouse**

- Keywords: **Neuropixels**, **Mouse**, **Head-fixed**, **Lateral Hypothalamus**, **Lateral Habenula**, **Prefrontal cortex**, **Aversion**

- Variables measured: **PupilTracking**, **ElectrodeGroup**, **ElectricalSeries**, **ProcessingModule**, **OptogeneticSeries**, **Units**, **LFP**, **BehavioralTimeSeries**

- Source paper: *Calvigioni, Daniela; Fuzik, Janos; Le Merre, Pierre; Slashcheva, Marina; Jung, Felix; Ortiz, Cantin; Lentini, Antonio; Csillag, Veronika; Graziano, Marta; Nikolakopoulou, Ifigeneia; Weglage, Moritz; Lazaridis, Iakovos; Kim, Hoseok; Lenzi, Irene; Park, Hyunsoo; Reinius, Björn; Carlén, Marie; Meletis, Konstantinos (2023) Esr1+ hypothalamic-habenula neurons shape aversive states*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000474">*[DANDI:000474](https://dandiarchive.org/dandiset/000474/draft)*: **EIS DATA**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Ezeh, Cynthia (2023) EIS DATA*

---

<a id="000476">*[DANDI:000476](https://dandiarchive.org/dandiset/000476/draft)*: **Neural recording of ventral striatum and pallidum in a probabilistic reward task**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **reinforcement learning, value function, basal ganglia, striatum, pallidum**

- Source paper: *Doya, Kenji (2023) Neural recording of ventral striatum and pallidum in a probabilistic reward task*

---

<a id="000477">*[DANDI:000477](https://dandiarchive.org/dandiset/000477/draft)*: **Dataset for Coregistration of heading to visual cues in retrosplenial cortex**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **77**, total size (MB): **694,959.86**

- Species: **Mus musculus - House mouse**

- Variables measured: **ImagingPlane**, **ProcessingModule**, **CompassDirection**, **OpticalChannel**, **Position**, **SpatialSeries**, **TwoPhotonSeries**, **PlaneSegmentation**

- Source paper: *Sit, Kevin (2023) Dataset for Coregistration of heading to visual cues in retrosplenial cortex*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000478">*[DANDI:000478](https://dandiarchive.org/dandiset/000478/draft)*: **BrainSTEM test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *C. Petersen, Peter (2023) BrainSTEM test*

---

<a id="000479">*[DANDI:000479](https://dandiarchive.org/dandiset/000479/draft)*: **BrainSTEM dataset**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Petersen, Peter C. (2023) BrainSTEM dataset*

---

<a id="000480">*[DANDI:000480](https://dandiarchive.org/dandiset/000480/draft)*: **Cellular Mechanisms of State-Dependent Processing in Visual Cortex (preliminary data)**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Bereshpolova, Yulia (2023) Cellular Mechanisms of State-Dependent Processing in Visual Cortex (preliminary data)*

---

<a id="000481">*[DANDI:000481](https://dandiarchive.org/dandiset/000481/draft)*: **State-dependent processing in visual cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **2**, total size (MB): **6.46**

- Species: **Oryctolagus cuniculus - Rabbits**

- Keywords: **electrophysiology, signal processing**

- Variables measured: **ElectrodeGroup**, **Units**, **ElectricalSeries**, **LFP**, **ProcessingModule**

- Source paper: *Bereshpolova, Yulia (2023) State-dependent processing in visual cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000481_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 3.23 MB | 
[File info](https://api.dandiarchive.org/api/assets/830ba7f9-1272-4279-ba7c-bd8aab0b89d8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000481/draft/files?location=sub-525%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/830ba7f9-1272-4279-ba7c-bd8aab0b89d8/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000482">*[DANDI:000482](https://dandiarchive.org/dandiset/000482/draft)*: **State-dependent processing in visual cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **1**, total size (MB): **79.94**

- Species: **Oryctolagus cuniculus - Rabbits**

- Variables measured: **LFP**, **ElectricalSeries**, **Units**, **ElectrodeGroup**, **ProcessingModule**

- Source paper: *Bereshpolova, Yulia (2023) State-dependent processing in visual cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000482_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 79.94 MB | 
[File info](https://api.dandiarchive.org/api/assets/f3c828ca-8ecd-4179-b70c-969b6107917f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000482/draft/files?location=sub-Elon%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f3c828ca-8ecd-4179-b70c-969b6107917f/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000483">*[DANDI:000483](https://dandiarchive.org/dandiset/000483/draft)*: **Dataset for "Coregistration of heading to visual cues in retrosplenial cortex"**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **128**, total size (MB): **695,653.68**

- Species: **Mus musculus - House mouse**

- Variables measured: **CompassDirection**, **OpticalChannel**, **PlaneSegmentation**, **SpatialSeries**, **ImagingPlane**, **Position**, **ProcessingModule**, **TwoPhotonSeries**

- Source paper: *Sit, Kevin; Goard, Michael (2023) Dataset for "Coregistration of heading to visual cues in retrosplenial cortex"*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000487">*[DANDI:000487](https://dandiarchive.org/dandiset/000487/draft)*: **Allen Institute Openscope - Tmp**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Allen Institute Openscope - Tmp (2023).*

---

<a id="000488">*[DANDI:000488](https://dandiarchive.org/dandiset/000488/draft)*: **Allen Institute Openscope - Differential encoding of temporal context and expectation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **43**, total size (MB): **61,460.3**

- Species: **Mus musculus - House mouse**

- Keywords: **neocortex**, **pyramidal neurons**, **two-photon calcium imaging**, **mouse VisP**, **prediction**, **predictive coding**

- Variables measured: **PlaneSegmentation**, **ImagingPlane**, **BehavioralTimeSeries**, **ProcessingModule**, **OpticalChannel**

- Source paper: *Lecoq, Jerome A.; Garrett, Marina; Choi, Hannah; Mazzucato, Luca; Wyrick, David (2023) Allen Institute Openscope - Differential encoding of temporal context and expectation*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000488_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 1219.9 MB | 
[File info](https://api.dandiarchive.org/api/assets/3f523944-d0de-4f30-ba91-79656ca3ad26) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000488/draft/files?location=sub-437812%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3f523944-d0de-4f30-ba91-79656ca3ad26/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 1236.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/63bf5bd6-9765-45ae-b5da-91eba0665bb9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000488/draft/files?location=sub-439885%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/63bf5bd6-9765-45ae-b5da-91eba0665bb9/download/) 
---

<a id="000489">*[DANDI:000489](https://dandiarchive.org/dandiset/000489/draft)*: **The impact of the second phase amplitude (% to the first phase) on the electroporation efficiency (measured as YP emission)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **18**, total size (MB): **18,594.42**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) The impact of the second phase amplitude (% to the first phase) on the electroporation efficiency (measured as YP emission)*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000489_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1021.67 MB | 
[File info](https://api.dandiarchive.org/api/assets/1e7fcc84-e5eb-4ead-802f-c26c91621306) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000489/draft/files?location=sub-Fig2-0-03%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1e7fcc84-e5eb-4ead-802f-c26c91621306/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1022.35 MB | 
[File info](https://api.dandiarchive.org/api/assets/f914475a-f6e3-4aef-b408-1acf9a679278) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000489/draft/files?location=sub-Fig2-0-06%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f914475a-f6e3-4aef-b408-1acf9a679278/download/) 
---

<a id="000490">*[DANDI:000490](https://dandiarchive.org/dandiset/000490/draft)*: **test set**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Dewberry, Savannah; Ezeh, Cynthia (2023) test set*

---

<a id="000491">*[DANDI:000491](https://dandiarchive.org/dandiset/000491/draft)*: **BrainFlowZZZ**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **14**, total size (MB): **5,324.8**

- Species: **Mus musculus - House mouse**

- Variables measured: **TwoPhotonSeries**, **ImagingPlane**, **OpticalChannel**, **ProcessingModule**, **PlaneSegmentation**

- Source paper: *Zhao, Yue; Boster, Kimberly; Kelley, Douglas; Raicevic, Nikola (2023) BrainFlowZZZ*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000491_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 240.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/a6c04ef2-21d9-451f-bdbe-859636968e5c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000491/draft/files?location=sub-BPN-OLD-M3%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a6c04ef2-21d9-451f-bdbe-859636968e5c/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 249.27 MB | 
[File info](https://api.dandiarchive.org/api/assets/3610bb59-13ea-4f4f-971f-68092354e1fe) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000491/draft/files?location=sub-BPN-M7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3610bb59-13ea-4f4f-971f-68092354e1fe/download/) 
---

<a id="000492">*[DANDI:000492](https://dandiarchive.org/dandiset/000492/draft)*: **Accelerated signal propagation speed in human neocortical microcircuits**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Olah, Gaspar (2023) Accelerated signal propagation speed in human neocortical microcircuits*

---

<a id="000529">*[DANDI:000529](https://dandiarchive.org/dandiset/000529/draft)*: **Test 2**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **27**, total size (MB): **5.27**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ElectrodeGroup**

- Source paper: *Dewberry, Savannah (2023) Test 2*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000529_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/88e6f549-aea2-4087-ae48-68638b05cafa) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000529/draft/files?location=sub-SIROF%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/88e6f549-aea2-4087-ae48-68638b05cafa/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/dfc9240a-541e-490a-8a46-fc7dc7ca6d2f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000529/draft/files?location=sub-RuOx%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/dfc9240a-541e-490a-8a46-fc7dc7ca6d2f/download/) 
---

<a id="000530">*[DANDI:000530](https://dandiarchive.org/dandiset/000530/draft)*: **Extracellular electrophysiology unit data from mouse Superior Colliculus during whisker guided virtual navigation**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Chinta, Suma (2023) Extracellular electrophysiology unit data from mouse Superior Colliculus during whisker guided virtual navigation*

---

<a id="000532">*[DANDI:000532](https://dandiarchive.org/dandiset/000532/draft)*: **Allen Institute Openscope - Tmp 2**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Lecoq, Jerome (2023) Allen Institute Openscope - Tmp 2*

---

<a id="000534">*[DANDI:000534](https://dandiarchive.org/dandiset/000534/draft)*: **to_be_deleted**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *to_be_deleted (2023).*

---

<a id="000535">*[DANDI:000535](https://dandiarchive.org/dandiset/000535/draft)*: **Allen Institute Openscope - Effects of Periodic Visual Stimulation on Neural Activity in Mouse Visual Cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **115**, total size (MB): **6,827.4**

- Species: **Mus musculus - House mouse**

- Keywords: **two-photon**, **cortical recording**, **gamma**, **neuroprotection**, **oscillations**, **visual stimuli**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **PlaneSegmentation**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Lecoq, Jerome; Murdock, Mitchell H.; Arkhipov, Anton; Ito, Shinya; Ren, Naixin; Billeh, Yazan N. (2023) Allen Institute Openscope - Effects of Periodic Visual Stimulation on Neural Activity in Mouse Visual Cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000535_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 7.94 MB | 
[File info](https://api.dandiarchive.org/api/assets/63b6a1be-3da5-4997-ae92-278401b0b5fe) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000535/draft/files?location=sub-509641%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/63b6a1be-3da5-4997-ae92-278401b0b5fe/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 7.94 MB | 
[File info](https://api.dandiarchive.org/api/assets/59eef0bb-cdc3-475a-933c-cd64cdb68022) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000535/draft/files?location=sub-525492%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/59eef0bb-cdc3-475a-933c-cd64cdb68022/download/) 
---

<a id="000536">*[DANDI:000536](https://dandiarchive.org/dandiset/000536/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *LI, YI (2023) test*

---

<a id="000537">*[DANDI:000537](https://dandiarchive.org/dandiset/000537/draft)*: **Scaling of GEVI Fluorescence with 1P and 2P Illumination**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **125**, total size (MB): **6,440.63**

- Species: **Homo sapiens - Human**

- Variables measured: 

- Source paper: *Adam Cohen (2023) Scaling of GEVI Fluorescence with 1P and 2P Illumination*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000537_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 43.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/c02995ae-a2ed-441b-b3e4-a0dc8c65a9c1) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000537/draft/files?location=sub-172658cell5q6a-900-700filter%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c02995ae-a2ed-441b-b3e4-a0dc8c65a9c1/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 43.29 MB | 
[File info](https://api.dandiarchive.org/api/assets/1fa16e7b-85da-446f-b7e4-91a161c4f916) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000537/draft/files?location=sub-175154cell14q6a-900-700filter%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1fa16e7b-85da-446f-b7e4-91a161c4f916/download/) 
---

<a id="000538">*[DANDI:000538](https://dandiarchive.org/dandiset/000538/draft)*: **Comparing the 1P and 2P Voltage Contrast of JEDI2P and Voltron2_JF525**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **11**, total size (MB): **1,954.27**

- Species: **Homo sapiens - Human**

- Variables measured: 

- Source paper: *Adam Cohen (2023) Comparing the 1P and 2P Voltage Contrast of JEDI2P and Voltron2_JF525*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000538_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 177.66 MB | 
[File info](https://api.dandiarchive.org/api/assets/a3b08f3a-46d6-466c-9763-5b5c3f57c322) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000538/draft/files?location=sub-180242Voltron2JF525cell3%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a3b08f3a-46d6-466c-9763-5b5c3f57c322/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 177.66 MB | 
[File info](https://api.dandiarchive.org/api/assets/0e26ddd2-1fd2-4bd5-b216-2d2d595eb695) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000538/draft/files?location=sub-182405Voltron2JF525cell4t1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0e26ddd2-1fd2-4bd5-b216-2d2d595eb695/download/) 
---

<a id="000539">*[DANDI:000539](https://dandiarchive.org/dandiset/000539/draft)*: **EDtest2**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Dimwamwa, Elaida (2023) EDtest2*

---

<a id="000540">*[DANDI:000540](https://dandiarchive.org/dandiset/000540/draft)*: **Dataset for: A change in behavioral state switches the pattern of motor output that underlies rhythmic head and orofacial movements**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **990**, total size (MB): **1,003,937.35**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **breathing**, **coupled oscillators**, **electromyogram**, **foraging**, **muscles**, **nose**, **preBotzinger complex**, **rearing**, **vibrissae**, **whiskers**, **neck**

- Variables measured: **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Liao, Song-Mao; Kleinfeld, David; Rinehart, Duane; University of California San Diego (2023) Dataset for: A change in behavioral state switches the pattern of motor output that underlies rhythmic head and orofacial movements*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000540_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 89.87 MB | 
[File info](https://api.dandiarchive.org/api/assets/e5a87e92-d243-4224-bf4a-f32c89b3fc34) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000540/draft/files?location=sub-SLR110%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e5a87e92-d243-4224-bf4a-f32c89b3fc34/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 104.7 MB | 
[File info](https://api.dandiarchive.org/api/assets/52ab55b7-09d6-40f1-93db-e1a39f961ecb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000540/draft/files?location=sub-SLR090%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/52ab55b7-09d6-40f1-93db-e1a39f961ecb/download/) 
---

<a id="000541">*[DANDI:000541](https://dandiarchive.org/dandiset/000541/draft)*: **NeuroPAL Microfluidic Chip Images and GCaMP activity**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **19**, total size (MB): **27,615.74**

- Species: **Caenorhabditis elegans**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**

- Source paper: *Sprague, Daniel (2023) NeuroPAL Microfluidic Chip Images and GCaMP activity*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000541_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-0**  
   Size: 1452.7 MB | 
[File info](https://api.dandiarchive.org/api/assets/e5f33fb4-3f23-4128-b19c-137c14378071) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000541/draft/files?location=sub-20190928-07%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e5f33fb4-3f23-4128-b19c-137c14378071/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-0**  
   Size: 1453.95 MB | 
[File info](https://api.dandiarchive.org/api/assets/f6ebc65c-53bb-4f94-be41-c64209c4c9fb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000541/draft/files?location=sub-20190925-04%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f6ebc65c-53bb-4f94-be41-c64209c4c9fb/download/) 
---

<a id="000542">*[DANDI:000542](https://dandiarchive.org/dandiset/000542/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Rinehart, Duane (2023) test*

---

<a id="000543">*[DANDI:000543](https://dandiarchive.org/dandiset/000543/draft)*: **Test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Liao, Song-Mao (2023) Test*

---

<a id="000544">*[DANDI:000544](https://dandiarchive.org/dandiset/000544/draft)*: **Test Dataset**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **3**, total size (MB): **971.76**

- Species: **Mus musculus - House mouse**

- Variables measured: **BehavioralEvents**, **BehavioralTimeSeries**, **Units**, **ElectrodeGroup**

- Source paper: *Bakshi, Kushal (2023) Test Dataset*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000544_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 485.78 MB | 
[File info](https://api.dandiarchive.org/api/assets/a87aab18-75dd-4c4c-b4f4-942ccfccb594) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000544/draft/files?location=sub-484677%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a87aab18-75dd-4c4c-b4f4-942ccfccb594/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000545">*[DANDI:000545](https://dandiarchive.org/dandiset/000545/draft)*: **Test set**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **1**, total size (MB): **0.19**

- Species: **Mus musculus - House mouse**

- Variables measured: 

- Source paper: *Bakshi, Kushal (2023) Test set*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000545_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 0.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/1f30f802-17dc-47db-abb9-da663e959ec0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000545/draft/files?location=sub-001%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1f30f802-17dc-47db-abb9-da663e959ec0/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000546">*[DANDI:000546](https://dandiarchive.org/dandiset/000546/draft)*: **vStr_phase_stim**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **1**, total size (MB): **7,785.86**

- Species: **Mus musculus - House mouse**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Christian, Horea (2023) vStr_phase_stim*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000547">*[DANDI:000547](https://dandiarchive.org/dandiset/000547/draft)*: **Perivascular Pumping of Cerebrospinal Fluid in the Brain with a Valve Mechanism**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **70**, total size (MB): **17,585.56**

- Species: **Mus musculus - House mouse**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **ProcessingModule**, **TwoPhotonSeries**

- Source paper: *Zhao, Yue; Gan, Yiming; Kelley, Douglas; Holstein-Rønsbo, Stephanie; Boster, Kimberly; Thomas, John; Nedergaard, Maiken (2023) Perivascular Pumping of Cerebrospinal Fluid in the Brain with a Valve Mechanism*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000547_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 176.98 MB | 
[File info](https://api.dandiarchive.org/api/assets/06c72ea1-a3de-4c52-895c-b21f6bc9da78) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000547/draft/files?location=sub-310%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/06c72ea1-a3de-4c52-895c-b21f6bc9da78/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 177.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/aef47a7d-979a-4491-bb62-f08bd0e16aa5) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000547/draft/files?location=sub-309%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/aef47a7d-979a-4491-bb62-f08bd0e16aa5/download/) 
---

<a id="000548">*[DANDI:000548](https://dandiarchive.org/dandiset/000548/draft)*: **Effect of the number of pulses on electroporation by unipolar and 50 % bipolar pulses**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **19**, total size (MB): **19,823.05**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei     (2023) Effect of the number of pulses on electroporation by unipolar and 50 % bipolar pulses*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000548_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1022.35 MB | 
[File info](https://api.dandiarchive.org/api/assets/ad15a104-b574-4855-b70a-903fb46c37ed) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000548/draft/files?location=sub-Fig3-Uni5-06%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ad15a104-b574-4855-b70a-903fb46c37ed/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1032.1 MB | 
[File info](https://api.dandiarchive.org/api/assets/4f327e1a-ab34-4d27-8650-65707978003c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000548/draft/files?location=sub-Fig3-Bi5-10%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4f327e1a-ab34-4d27-8650-65707978003c/download/) 
---

<a id="000549">*[DANDI:000549](https://dandiarchive.org/dandiset/000549/draft)*: **Effect of the pulse duration on electroporation by unipolar and 50% bipolar pulses**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **26**, total size (MB): **40,412.79**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) Effect of the pulse duration on electroporation by unipolar and 50% bipolar pulses*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000549_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1010.86 MB | 
[File info](https://api.dandiarchive.org/api/assets/ecd4cc5c-41bb-4c07-b20f-9b3036da1109) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000549/draft/files?location=sub-Fig4-5-Bi300ns-04%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ecd4cc5c-41bb-4c07-b20f-9b3036da1109/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1013.64 MB | 
[File info](https://api.dandiarchive.org/api/assets/948fe67d-2b46-4902-8f06-21a24f6c0fc2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000549/draft/files?location=sub-Fig4-5-Bi300ns-08%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/948fe67d-2b46-4902-8f06-21a24f6c0fc2/download/) 
---

<a id="000550">*[DANDI:000550](https://dandiarchive.org/dandiset/000550/draft)*: **Pulse repetition rate**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **17**, total size (MB): **23,579.02**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii ; Semenov, Iurii; Pakhomov, Andrei (2023) Pulse repetition rate*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000550_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1027.67 MB | 
[File info](https://api.dandiarchive.org/api/assets/ab88ec8f-eda9-4ba9-af0d-a4f8c0e299cd) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000550/draft/files?location=sub-Fig6-5xBi-0,83MHz-13%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ab88ec8f-eda9-4ba9-af0d-a4f8c0e299cd/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1028.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/b443d5fb-c8ae-4257-aa97-349db34cd9a0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000550/draft/files?location=sub-Fig6-5xBi-100kHz-11%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b443d5fb-c8ae-4257-aa97-349db34cd9a0/download/) 
---

<a id="000551">*[DANDI:000551](https://dandiarchive.org/dandiset/000551/draft)*: **Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Valero, Manuel (2023) Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics*

---

<a id="000552">*[DANDI:000552](https://dandiarchive.org/dandiset/000552/draft)*: **Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **117**, total size (MB): **1,545,387.84**

- Species: **Mus musculus - House mouse**

- Keywords: **Hippocampus**, **Neural circuits**, **Development of the nervous system**

- Variables measured: **ElectricalSeries**, **ProcessingModule**, **ElectrodeGroup**, **LFP**, **SpatialSeries**, **Position**, **Units**

- Source paper: *Huszár, Roman; Zhang, Yunchang; Blockus, Heike; Buzsáki, György (2023) Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000552_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 19.47 MB | 
[File info](https://api.dandiarchive.org/api/assets/b2bc6332-5cf3-4a65-b1a4-0a712dd4b873) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000552/draft/files?location=sub-e13-1m1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b2bc6332-5cf3-4a65-b1a4-0a712dd4b873/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 22.45 MB | 
[File info](https://api.dandiarchive.org/api/assets/66b3cd92-13f7-4411-aae4-f1a06875dc98) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000552/draft/files?location=sub-e14-1m1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/66b3cd92-13f7-4411-aae4-f1a06875dc98/download/) 
---

<a id="000554">*[DANDI:000554](https://dandiarchive.org/dandiset/000554/draft)*: **Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **36**, total size (MB): **129,066.8**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Tchoe, Youngbin (2023) Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000555">*[DANDI:000555](https://dandiarchive.org/dandiset/000555/draft)*: **Conserved neural dynamics across species in olfaction**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Moss, Elizabeth (2023) Conserved neural dynamics across species in olfaction*

---

<a id="000556">*[DANDI:000556](https://dandiarchive.org/dandiset/000556/draft)*: **First set**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Zhang, James (2023) First set*

---

<a id="000557">*[DANDI:000557](https://dandiarchive.org/dandiset/000557/draft)*: **Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Tchoe, Youngbin (2023) Human brain mapping with multithousand-channel PtNRGrids resolves spatiotemporal dynamics*

---

<a id="000558">*[DANDI:000558](https://dandiarchive.org/dandiset/000558/draft)*: **Climbing fiber multi-innervation of mouse Purkinje dendrites with arborization common to human**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Busch, Silas (2023) Climbing fiber multi-innervation of mouse Purkinje dendrites with arborization common to human*

---

<a id="000559">*[DANDI:000559](https://dandiarchive.org/dandiset/000559/draft)*: **Spontaneous behaviour is structured by reinforcement without explicit reward**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **4360**, total size (MB): **14,078,285.64**

- Species: **Homo sapiens - Human**

- Keywords: **Basal Ganglia**, **Neural circuits**, **Reward**

- Variables measured: **ImagingPlane**, **OpticalChannel**, **OptogeneticSeries**, **ProcessingModule**, **Position**, **SpatialSeries**, **CompassDirection**

- Source paper: *Markowitz, Jeffrey E.; Gillis, Winthrop; Jay, Maya; Wood, Jeffrey; Harris, Ryley W.; Cieszkowski, Robert; Scott, Rebecca; Brann, David; Koveal, Dorothy; Kula, Tomasz; Weinreb, Caleb; Osman, Mohammed Abdal Monium ; Pinto, Sandra Romero ; Uchida, Naoshige ; Linderman, Scott W.; Sabatini, Bernardo; Datta, Sandeep Robert  (2024) Spontaneous behaviour is structured by reinforcement without explicit reward*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000559_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 120.49 MB | 
[File info](https://api.dandiarchive.org/api/assets/925b8d77-7360-475b-88c7-f3d79d7d7d68) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000559/draft/files?location=sub-dms-dlight-6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/925b8d77-7360-475b-88c7-f3d79d7d7d68/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 129.65 MB | 
[File info](https://api.dandiarchive.org/api/assets/390d347d-8425-4198-bd23-2635efda142f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000559/draft/files?location=sub-dls-dlight-8%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/390d347d-8425-4198-bd23-2635efda142f/download/) 
---

<a id="000560">*[DANDI:000560](https://dandiarchive.org/dandiset/000560/draft)*: **Calcium imaging of odor responses in the fruit fly mushroom body**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Srinivasan, Shyam (2023) Calcium imaging of odor responses in the fruit fly mushroom body*

---

<a id="000561">*[DANDI:000561](https://dandiarchive.org/dandiset/000561/draft)*: **32-CH Local Field Potential Data During Probabilistic Reversal Learning Task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **253**, total size (MB): **21,349.61**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: 

- Source paper: *Koloski, Miranda  (2023) 32-CH Local Field Potential Data During Probabilistic Reversal Learning Task*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000561_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/906749cb-a294-42d5-8879-2a5673501840) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000561/draft/files?location=sub-192%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/906749cb-a294-42d5-8879-2a5673501840/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/355e758a-90fc-4828-bef0-7d2842104b20) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000561/draft/files?location=sub-185%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/355e758a-90fc-4828-bef0-7d2842104b20/download/) 
---

<a id="000564">*[DANDI:000564](https://dandiarchive.org/dandiset/000564/draft)*: **microwave neuromodulation**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Cheng, Ji-Xin (2023) microwave neuromodulation*

---

<a id="000565">*[DANDI:000565](https://dandiarchive.org/dandiset/000565/draft)*: **C. elegans whole-brain neuroPAL and immobilized calcium imaging**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **37**, total size (MB): **75,296.8**

- Species: **Caenorhabditis elegans**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**

- Source paper: *Sprague, Daniel; Dunn, Raymond (2023) C. elegans whole-brain neuroPAL and immobilized calcium imaging*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000565_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-0**  
   Size: 253.71 MB | 
[File info](https://api.dandiarchive.org/api/assets/79d3a9d6-8314-431f-b320-98bad02cef8c) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000565/draft/files?location=sub-20221106-21-00-09%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/79d3a9d6-8314-431f-b320-98bad02cef8c/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-0**  
   Size: 253.71 MB | 
[File info](https://api.dandiarchive.org/api/assets/3515cee9-b3d5-4b50-8b8b-40f5a7c44af7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000565/draft/files?location=sub-20221028-18-48-00%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/3515cee9-b3d5-4b50-8b8b-40f5a7c44af7/download/) 
---

<a id="000566">*[DANDI:000566](https://dandiarchive.org/dandiset/000566/draft)*: **ASAP4 data**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **1**, total size (MB): **631.79**

- Species: **Drosophila melanogaster - Fruit fly**

- Variables measured: **ImagingPlane**, **OpticalChannel**, **TwoPhotonSeries**

- Source paper: *Lin, Michael (2023) ASAP4 data*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000566_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 631.79 MB | 
[File info](https://api.dandiarchive.org/api/assets/91a4b9c2-17e5-4da4-a718-d3682873f6e6) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000566/draft/files?location=sub-fly01%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/91a4b9c2-17e5-4da4-a718-d3682873f6e6/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000567">*[DANDI:000567](https://dandiarchive.org/dandiset/000567/draft)*: **Tested**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Yin, Jiaze (2023) Tested*

---

<a id="000568">*[DANDI:000568](https://dandiarchive.org/dandiset/000568/draft)*: **Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **138**, total size (MB): **904,756.92**

- Species: **Mus musculus - House mouse**

- Variables measured: **LFP**, **Units**, **SpatialSeries**, **ElectrodeGroup**, **ElectricalSeries**, **Position**, **ProcessingModule**, **OptogeneticSeries**

- Source paper: *Valero, Manuel;  Zutshi, Ipshita; Yoon, Euisik; Buzsáki, György (2023) Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000568_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 7.16 MB | 
[File info](https://api.dandiarchive.org/api/assets/e7e5f461-ae0a-4d56-aed4-b89ff2ca8a22) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000568/draft/files?location=sub-fCamk2%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e7e5f461-ae0a-4d56-aed4-b89ff2ca8a22/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 18.01 MB | 
[File info](https://api.dandiarchive.org/api/assets/fa6cff6b-633b-4fbe-a1e0-737a23458a6d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000568/draft/files?location=sub-fCamk1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/fa6cff6b-633b-4fbe-a1e0-737a23458a6d/download/) 
---

<a id="000569">*[DANDI:000569](https://dandiarchive.org/dandiset/000569/draft)*: **20230630_AIBS_Patchseq_nonhuman_primate**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **103**, total size (MB): **5,622.63**

- Species: **Macaca nemestrina - Pigtail macaque**

- Keywords: **Patch-seq**, **non-human primate**, **multimodal**

- Variables measured: **VoltageClampStimulusSeries**, **CurrentClampStimulusSeries**, **ProcessingModule**, **CurrentClampSeries**, **VoltageClampSeries**

- Source paper: *Mei, Nicholas; Lee, Brian; Kalmbach, Brian; Dalley, Rachel; Lein, Ed (2023) 20230630_AIBS_Patchseq_nonhuman_primate*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000569_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 25.65 MB | 
[File info](https://api.dandiarchive.org/api/assets/c69ed191-c27c-4e63-901a-38c414875342) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000569/draft/files?location=sub-1223010848%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c69ed191-c27c-4e63-901a-38c414875342/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 25.97 MB | 
[File info](https://api.dandiarchive.org/api/assets/f9a896d5-a007-4f19-a80c-6d0650e9356a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000569/draft/files?location=sub-1257702203%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f9a896d5-a007-4f19-a80c-6d0650e9356a/download/) 
---

<a id="000570">*[DANDI:000570](https://dandiarchive.org/dandiset/000570/draft)*: **20230630_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **155**, total size (MB): **4,628.3**

- Species: **Homo sapiens - Human**

- Keywords: **Patch-seq**, **human**, **multimodal**

- Variables measured: **ProcessingModule**, **VoltageClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Mei, Nicholas; Lee, Brian; Kalmbach, Brian; Chartrand, Tom; Dalley, Rachel; Lein, Ed (2023) 20230630_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000570_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 13.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/2ecbc097-e4bc-408b-afab-9cf43ab57e14) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000570/draft/files?location=sub-665691251%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2ecbc097-e4bc-408b-afab-9cf43ab57e14/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 14.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/8f529ffc-2433-423f-b37c-65fc4371933f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000570/draft/files?location=sub-731978186%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8f529ffc-2433-423f-b37c-65fc4371933f/download/) 
---

<a id="000571">*[DANDI:000571](https://dandiarchive.org/dandiset/000571/draft)*: **Intracranial recordings using BCI2000 and the CorTec BrainInterchange**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **201**, total size (MB): **195.38**

- Variables measured: 

- Source paper: *Mivalt, Filip; van den Boom, Max; Brunner, Peter; Kim, Jiwon; Duque-Lopez, Andrea; Krakorova, Martina; Kim, Inyong; Chang, Su-youne; Hermes, Dora; Miller, Kai J.; Kremen, Vaclav; Worrell, Gregory A. (2023) Intracranial recordings using BCI2000 and the CorTec BrainInterchange*

---

<a id="000572">*[DANDI:000572](https://dandiarchive.org/dandiset/000572/draft)*: **Activity map of a cortico-cerebellar loop underlying motor planning**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **289**, total size (MB): **311,812.04**

- Species: **Mus musculus - House mouse**

- Variables measured: **OptogeneticSeries**, **SpikeEventSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Activity map of a cortico-cerebellar loop underlying motor planning (2023).*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000572_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 400.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/34b041ef-876d-4f6e-87d5-2a74ab8ad83a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000572/draft/files?location=sub-BAYLORZJP01%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/34b041ef-876d-4f6e-87d5-2a74ab8ad83a/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 424.89 MB | 
[File info](https://api.dandiarchive.org/api/assets/a65ef979-276e-495f-ae84-a9fe0d1df203) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000572/draft/files?location=sub-BAYLORNL28%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a65ef979-276e-495f-ae84-a9fe0d1df203/download/) 
---

<a id="000574">*[DANDI:000574](https://dandiarchive.org/dandiset/000574/draft)*: **Dataset of human medial temporal lobe neurons, scalp and intracranial EEG during a verbal working memory task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **43**, total size (MB): **127,123.75**

- Species: **Homo sapiens - Human**

- Keywords: **Electrophysiology **, **Human**, **Awake**, **Local field potential**, **Neuronal action potential**, **Spikes**, **Medial temporal lobe**, **Hippocampus**, **Entorhinal cortex**, **Amygdala**, **Scalp EEG**, **Intracranial EEG**, **Cognitive task**, **Verbal working memory**, **Epilepsy**

- Variables measured: **Units**, **LFP**, **ElectrodeGroup**, **ElectricalSeries**, **ProcessingModule**, **BehavioralEvents**

- Source paper: *Boran, Ece; Fedele, Tommaso; Hilfiker, Peter; Stieglitz, Lennart; Grunwald, Thomas; Hohenheim, Jan; Sarnthein, Johannes (2023) Dataset of human medial temporal lobe neurons, scalp and intracranial EEG during a verbal working memory task*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000574_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 1355.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/4fa2605b-16dd-47e9-a083-5a853f46c000) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000574/draft/files?location=sub-05%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4fa2605b-16dd-47e9-a083-5a853f46c000/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 1381.36 MB | 
[File info](https://api.dandiarchive.org/api/assets/a557a7a9-2bb2-4b89-832d-934e77a77c73) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000574/draft/files?location=sub-01%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a557a7a9-2bb2-4b89-832d-934e77a77c73/download/) 
---

<a id="000575">*[DANDI:000575](https://dandiarchive.org/dandiset/000575/draft)*: **Dataset of human medial temporal lobe neurons during a visual working memory task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **17**, total size (MB): **44,196.03**

- Species: **Homo sapiens - Human**

- Variables measured: **Units**, **BehavioralEvents**, **ElectrodeGroup**, **ProcessingModule**, **LFP**, **ElectricalSeries**

- Source paper: *Boran, Ece; Hilfiker, Peter; Stieglitz, Lennart ; Hohenheim, Jan; Klaver, Peter; Sarnthein, Johannes  (2023) Dataset of human medial temporal lobe neurons during a visual working memory task*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000575_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.72 MB | 
[File info](https://api.dandiarchive.org/api/assets/ba30fc51-fabb-4f09-b773-b783b6f17d95) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000575/draft/files?location=sub-12%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ba30fc51-fabb-4f09-b773-b783b6f17d95/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.82 MB | 
[File info](https://api.dandiarchive.org/api/assets/e96a31c3-b4c2-434b-979e-8d7b56f0b635) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000575/draft/files?location=sub-02%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e96a31c3-b4c2-434b-979e-8d7b56f0b635/download/) 
---

<a id="000576">*[DANDI:000576](https://dandiarchive.org/dandiset/000576/draft)*: **Dataset of neurons and intracranial EEG from human amygdala during aversive dynamic visual stimulation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **11**, total size (MB): **196.06**

- Species: **Homo sapiens - Human**

- Variables measured: **ProcessingModule**, **LFP**, **Units**, **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Fedele, Tommaso; Hilfiker, Peter ; Grunwald, Thomas ; Stieglitz, Lennart ; Jokeit, Hennric; Hohenheim, Jan; Sarnthein, Johannes  (2023) Dataset of neurons and intracranial EEG from human amygdala during aversive dynamic visual stimulation*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000576_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 14.06 MB | 
[File info](https://api.dandiarchive.org/api/assets/f1b3e78b-adfb-414c-96ea-7a3cea89a6cb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000576/draft/files?location=sub-08%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f1b3e78b-adfb-414c-96ea-7a3cea89a6cb/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 14.06 MB | 
[File info](https://api.dandiarchive.org/api/assets/20f45cda-1732-4692-a18f-51f3ea3e1d1e) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000576/draft/files?location=sub-05%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/20f45cda-1732-4692-a18f-51f3ea3e1d1e/download/) 
---

<a id="000577">*[DANDI:000577](https://dandiarchive.org/dandiset/000577/draft)*: **Emergence of Agency in Human Infants**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **behavioral neuroscience**, **complex systems**, **coordination dynamics**, **self-organization**, **agency**, **developmental psychology**, **infancy**, **timeseries**, **mocap**

- Source paper: *Sloan, Aliza (2023) Emergence of Agency in Human Infants*

---

<a id="000579">*[DANDI:000579](https://dandiarchive.org/dandiset/000579/draft)*: **Two-photon calcium imaging of mouse posterior cortical areas during dynamic navigation decisions (Tseng et al., 2022, Neuron)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **308**, total size (MB): **245,591.97**

- Species: **Mus musculus - House mouse**

- Keywords: **mouse**, **cortex**, **decision-making**, **navigation**, **virtual reality**, **two-photon imaging**, **posterior cortex**, **posterior parietal cortex**, **retrosplenial cortex**, **visual cortex**, **rule-switching**, **flexible decisions**, **retrograde labeling**

- Variables measured: **ImagingPlane**, **ProcessingModule**, **OpticalChannel**, **Position**, **SpatialSeries**, **BehavioralTimeSeries**, **PlaneSegmentation**

- Source paper: *Tseng, Shih-Yi; Chettih, Selmaan; Harvey, Christopher (2023) Two-photon calcium imaging of mouse posterior cortical areas during dynamic navigation decisions (Tseng et al., 2022, Neuron)*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000579_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 267.0 MB | 
[File info](https://api.dandiarchive.org/api/assets/2332537e-2b80-4a52-a1f0-aa38f9b43399) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000579/draft/files?location=sub-10%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/2332537e-2b80-4a52-a1f0-aa38f9b43399/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 267.0 MB | 
[File info](https://api.dandiarchive.org/api/assets/080f2b2e-a591-4353-bcbe-573c1cb29846) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000579/draft/files?location=sub-6%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/080f2b2e-a591-4353-bcbe-573c1cb29846/download/) 
---

<a id="000582">*[DANDI:000582](https://dandiarchive.org/dandiset/000582/draft)*: **Conjunctive Representation of Position, Direction, and Velocity in Entorhinal Cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **115**, total size (MB): **1,812.38**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ElectricalSeries**, **Position**, **Units**, **ElectrodeGroup**, **ProcessingModule**, **LFP**, **SpatialSeries**

- Source paper: *Sargolini, Francesca; Fyhn, Marianne; Hafting, Torkel; McNaughton, Bruce L.; Witter, Menno P.; Moser, May-Britt; Moser, Edvard I.; Waade, Haagen; Ball, Simon (2023) Conjunctive Representation of Position, Direction, and Velocity in Entorhinal Cortex*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000582_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 3.75 MB | 
[File info](https://api.dandiarchive.org/api/assets/4718021c-98c7-4241-95b8-09be6e7dbacb) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000582/draft/files?location=sub-10884%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4718021c-98c7-4241-95b8-09be6e7dbacb/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 10.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/a1b081bb-7d0a-4c2f-8fb7-5639fce88aa8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000582/draft/files?location=sub-10697%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a1b081bb-7d0a-4c2f-8fb7-5639fce88aa8/download/) 
---

<a id="000615">*[DANDI:000615](https://dandiarchive.org/dandiset/000615/draft)*: **A Novel Neuropathic Pain Treatment: Achieving Neuronal Inhibition with a Splti Ring Resonator**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **1**, total size (MB): **1,805.45**

- Species: **Procambarus clarkii - Red swamp crayfish**

- Variables measured: 

- Source paper: *Cherepashensky, Mark (2023) A Novel Neuropathic Pain Treatment: Achieving Neuronal Inhibition with a Splti Ring Resonator*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000618">*[DANDI:000618](https://dandiarchive.org/dandiset/000618/draft)*: **SpikeForest ground truth datasets**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **124**, total size (MB): **145,521.72**

- Species: **Mus musculus - House mouse**

- Variables measured: **Units**, **ElectricalSeries**, **ElectrodeGroup**, **ProcessingModule**

- Source paper: *Magland, Jeremy; Jun, James J; Lovero, Elizabeth; Morley, Alexander J; Hurwitz, Cole Lincoln; Buccino, Alessio Paolo; Garcia, Samuel; Barnett, Alex H; English, Daniel (2023) SpikeForest ground truth datasets*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000618_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.92 MB | 
[File info](https://api.dandiarchive.org/api/assets/99fcc628-1cf2-46f2-bfdc-0fe8985b42c7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000618/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/99fcc628-1cf2-46f2-bfdc-0fe8985b42c7/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 25.41 MB | 
[File info](https://api.dandiarchive.org/api/assets/fa7562ee-e978-425e-a07a-02165a698612) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000618/draft/files?location=) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/fa7562ee-e978-425e-a07a-02165a698612/download/) 
---

<a id="000619">*[DANDI:000619](https://dandiarchive.org/dandiset/000619/draft)*: **Benisty_Higley_2023**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Higley, Michael (2023) Benisty_Higley_2023*

---

<a id="000623">*[DANDI:000623](https://dandiarchive.org/dandiset/000623/draft)*: **Data for: Multimodal brain responses during movie watching: single-neuron, intracranial EEG, and fMRI in human patients**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **29**, total size (MB): **27,744.75**

- Species: **Homo sapiens - Human**

- Keywords: **movie watching**, **recognition memory**, **single-neuron**, **iEEG**

- Variables measured: **ElectricalSeries**, **LFP**, **EyeTracking**, **ElectrodeGroup**, **BehavioralTimeSeries**, **PupilTracking**, **SpatialSeries**, **ProcessingModule**, **Units**

- Source paper: *Keles, Umit; Dubois, Julien; Le, Kevin J. M.; Tyszka, J. Michael; Kahn, David A.; Reed, Chrystal M.; Chung, Jeffrey M. ; Mamelak, Adam N.; Adolphs, Ralph; Rutishauser, Ueli (2024) Data for: Multimodal brain responses during movie watching: single-neuron, intracranial EEG, and fMRI in human patients*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000623_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 548.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/aea3c535-a69a-41a6-9ffc-ceea9c7e6bae) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000623/draft/files?location=sub-CS62%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/aea3c535-a69a-41a6-9ffc-ceea9c7e6bae/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 803.88 MB | 
[File info](https://api.dandiarchive.org/api/assets/ffcb1836-587e-42f4-887b-50b02948b779) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000623/draft/files?location=sub-CS41%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ffcb1836-587e-42f4-887b-50b02948b779/download/) 
---

<a id="000624">*[DANDI:000624](https://dandiarchive.org/dandiset/000624/draft)*: **A brainstem circuit for the expression of defensive facial reactions in rat**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **45**, total size (MB): **130,570.93**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **ProcessingModule**, **Units**, **BehavioralEvents**

- Source paper: *Rinehart, Duane; Amalia Callado-Pérez; Kleinfeld, David; Fassihi, Arash; Dechênes, Martin; Moore, Jeffrey D.; Demers, Maxime (2023) A brainstem circuit for the expression of defensive facial reactions in rat*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000624_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/e095fd65-120b-4ed0-83d8-23bc279d0b42) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000624/draft/files?location=sub-Rat335%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e095fd65-120b-4ed0-83d8-23bc279d0b42/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.19 MB | 
[File info](https://api.dandiarchive.org/api/assets/43d3c226-05fc-414c-8bb1-c86a83f2bb29) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000624/draft/files?location=sub-Rat332%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/43d3c226-05fc-414c-8bb1-c86a83f2bb29/download/) 
---

<a id="000625">*[DANDI:000625](https://dandiarchive.org/dandiset/000625/draft)*: **Molecularly Identified CA1 Interneuron Dynamics**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **3**, total size (MB): **74.9**

- Species: **Mus musculus - House mouse**

- Keywords: **2-photon calcium imaging**, **interneuron**, **hippocampus**, **ca1**, **mouse**, **head-fixed**, **treadmill**, **Losonczy Lab**, **Columbia University**

- Variables measured: **BehavioralEpochs**, **ProcessingModule**, **SpatialSeries**, **TwoPhotonSeries**, **Position**, **ImagingPlane**, **OpticalChannel**, **PlaneSegmentation**

- Source paper: *Geiller, Tristan (2023) Molecularly Identified CA1 Interneuron Dynamics*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000625_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 24.71 MB | 
[File info](https://api.dandiarchive.org/api/assets/274df0e2-a678-4d74-8e6a-99953eefbb47) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000625/draft/files?location=sub-tg19%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/274df0e2-a678-4d74-8e6a-99953eefbb47/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000626">*[DANDI:000626](https://dandiarchive.org/dandiset/000626/draft)*: **Neural Organoid Ephys Trace**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **1**, total size (MB): **18.3**

- Species: **Macaca mulatta - Rhesus monkey**

- Variables measured: **ProcessingModule**

- Source paper: *Blauvelt, Lon (2023) Neural Organoid Ephys Trace*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000626_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 18.3 MB | 
[File info](https://api.dandiarchive.org/api/assets/24c3c83d-bd37-4f00-b420-d3c36e09b24a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000626/draft/files?location=sub-monk-g%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/24c3c83d-bd37-4f00-b420-d3c36e09b24a/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000628">*[DANDI:000628](https://dandiarchive.org/dandiset/000628/draft)*: **Extracellular recording along macaque ventral stream during natural image free viewing**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **2037**, total size (MB): **52,741.3**

- Species: **Macaca mulatta - Rhesus monkey**

- Keywords: **Macaque**, **Ventral stream**, **Free viewing**, **Natural images**, **Extracellular electrophysiology**

- Variables measured: **EyeTracking**, **SpatialSeries**, **ProcessingModule**

- Source paper: *Xiao, Will; Sharma, Saloni; Kreiman, Gabriel; Livingstone, Margaret; National Institutes of Health (2023) Extracellular recording along macaque ventral stream during natural image free viewing*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000628_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/e9f25cc3-bc88-4c4f-8543-12173c6084cc) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000628/draft/files?location=sub-Bf%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e9f25cc3-bc88-4c4f-8543-12173c6084cc/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/02c2a27e-ce0a-4b23-b789-b88ac00ea1f7) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000628/draft/files?location=sub-Ve%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/02c2a27e-ce0a-4b23-b789-b88ac00ea1f7/download/) 
---

<a id="000629">*[DANDI:000629](https://dandiarchive.org/dandiset/000629/draft)*: **Gillespie et al (2024) Neurofeedback training can modulate task-relevant memory replay rate in rats**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **114**, total size (MB): **16,808,409.96**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **Position**, **ElectricalSeries**, **ProcessingModule**, **SpatialSeries**, **BehavioralEvents**

- Source paper: *Gillespie, Anna; Denovellis, Eric; Frank, Loren; Desse, Sachi; Astudillo Maya, Daniela (2023) Gillespie et al (2024) Neurofeedback training can modulate task-relevant memory replay rate in rats*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000630">*[DANDI:000630](https://dandiarchive.org/dandiset/000630/draft)*: **Human L1 patch-seq electrophysiology**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **210**, total size (MB): **8,073.13**

- Species: **Human**

- Keywords: **human**, **multimodal**, **patch-seq**, **neocortex**

- Variables measured: **ProcessingModule**, **VoltageClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Chartrand, Thomas; Lee, Brian; Dalley, Rachel; Lein, Ed; Kalmbach, Brian (2023) Human L1 patch-seq electrophysiology*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000630_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 15.15 MB | 
[File info](https://api.dandiarchive.org/api/assets/0f28edea-b0b3-46de-bef6-bd061b6b564f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000630/draft/files?location=sub-700619648%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0f28edea-b0b3-46de-bef6-bd061b6b564f/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 15.55 MB | 
[File info](https://api.dandiarchive.org/api/assets/b6894865-4680-4851-be6e-1d7e29619418) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000630/draft/files?location=sub-596832620%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b6894865-4680-4851-be6e-1d7e29619418/download/) 
---

<a id="000631">*[DANDI:000631](https://dandiarchive.org/dandiset/000631/draft)*: **Effect of the electric field vector change on the electroporation efficiency of paired-pulse trains compared to single-pulse trains**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **15**, total size (MB): **18,379.96**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) Effect of the electric field vector change on the electroporation efficiency of paired-pulse trains compared to single-pulse trains*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000631_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1040.65 MB | 
[File info](https://api.dandiarchive.org/api/assets/5c4ff26e-bced-4632-bffa-9db2c182c122) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000631/draft/files?location=sub-600ns-5kV-1HzUP-7-31-21-BPAE-10%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/5c4ff26e-bced-4632-bffa-9db2c182c122/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1041.97 MB | 
[File info](https://api.dandiarchive.org/api/assets/cfb37f51-3ef6-41d3-8b38-1f39c56cd704) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000631/draft/files?location=sub-600ns-5kV-1HzUP-8-9-21-BPAE-14%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/cfb37f51-3ef6-41d3-8b38-1f39c56cd704/download/) 
---

<a id="000632">*[DANDI:000632](https://dandiarchive.org/dandiset/000632/draft)*: **Electroporation efficiency of co-directional and cross-directional paired pulses**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **24**, total size (MB): **42,744.12**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) Electroporation efficiency of co-directional and cross-directional paired pulses*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000633">*[DANDI:000633](https://dandiarchive.org/dandiset/000633/draft)*: **The difference in electroporation patterns produced by a train of single pulses and a train of paired pulses**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **2**, total size (MB): **2,137.42**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) The difference in electroporation patterns produced by a train of single pulses and a train of paired pulses*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000633_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 1077.54 MB | 
[File info](https://api.dandiarchive.org/api/assets/e227c013-22d7-4bd9-a567-85468e85b2e3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000633/draft/files?location=sub-Single-pulse-trains%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e227c013-22d7-4bd9-a567-85468e85b2e3/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000634">*[DANDI:000634](https://dandiarchive.org/dandiset/000634/draft)*: **Cell Membrane Charging by Co- and Counter-Directional ns electrical pulses (nsEP)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **10**, total size (MB): **1,035.53**

- Species: **Cricetulus griseus - Cricetulus aureus**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii; Pakhomov, Andrei (2023) Cell Membrane Charging by Co- and Counter-Directional ns electrical pulses (nsEP)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000634_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 101.4 MB | 
[File info](https://api.dandiarchive.org/api/assets/7dc56eb6-8258-4678-98c7-fc1e1cdd7983) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000634/draft/files?location=sub-ground2204-15%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7dc56eb6-8258-4678-98c7-fc1e1cdd7983/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 101.47 MB | 
[File info](https://api.dandiarchive.org/api/assets/80a9300a-d680-40d6-8279-f19a5c4db450) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000634/draft/files?location=sub-ground2204-16%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/80a9300a-d680-40d6-8279-f19a5c4db450/download/) 
---

<a id="000635">*[DANDI:000635](https://dandiarchive.org/dandiset/000635/draft)*: **20230930_AIBS_Patchseq_nonhuman_primate**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **81**, total size (MB): **4,707.14**

- Species: **Macaca nemestrina**

- Keywords: **Patch-seq**, **non-human primate**, **multimodal**

- Variables measured: **CurrentClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampSeries**, **ProcessingModule**, **VoltageClampStimulusSeries**

- Source paper: *Soliman, Sherif; Lee, Brian; Allen Institute for Brian Science; National Institute of Mental Health; Kalmbach, Brian; Dalley, Rachel; Lein, Ed (2023) 20230930_AIBS_Patchseq_nonhuman_primate*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000635_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 25.99 MB | 
[File info](https://api.dandiarchive.org/api/assets/e610a258-634a-458a-b635-e6c2641b7228) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000635/draft/files?location=sub-1271976045%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e610a258-634a-458a-b635-e6c2641b7228/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 26.9 MB | 
[File info](https://api.dandiarchive.org/api/assets/eaaae56e-99d5-4203-aae8-2cd08fa0994b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000635/draft/files?location=sub-1273579455%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/eaaae56e-99d5-4203-aae8-2cd08fa0994b/download/) 
---

<a id="000636">*[DANDI:000636](https://dandiarchive.org/dandiset/000636/draft)*: **Human interneuron patch-seq electrophysiology**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **706**, total size (MB): **24,473.83**

- Species: **Human**

- Keywords: **human**, **multimodal**, **patch-seq**, **neocortex**

- Variables measured: **ProcessingModule**, **VoltageClampSeries**, **CurrentClampStimulusSeries**, **VoltageClampStimulusSeries**, **CurrentClampSeries**

- Source paper: *Lee, Brian; Dalley, Rachel; Chartrand, Thomas; Kalmbach, Brian; Lein, Ed (2023) Human interneuron patch-seq electrophysiology*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000636_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 12.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/c40d0858-94b7-454d-80bc-9d7836c6c294) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000636/draft/files?location=sub-720619787%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c40d0858-94b7-454d-80bc-9d7836c6c294/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 13.18 MB | 
[File info](https://api.dandiarchive.org/api/assets/7507c554-12ab-4a97-a51e-06f8e995c6ad) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000636/draft/files?location=sub-643488707%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7507c554-12ab-4a97-a51e-06f8e995c6ad/download/) 
---

<a id="000637">*[DANDI:000637](https://dandiarchive.org/dandiset/000637/draft)*: **Neural Spike Time Response Data in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.5.0**), file count: **292**, total size (MB): **1,163.42**

- Species: **Rattus norvegicus - Norway rat**

- Variables measured: **Units**, **ElectrodeGroup**

- Source paper: *Ramachandran, Sandhya; Gao, Huan; He, Bin; Yu, Kai (2023) Neural Spike Time Response Data in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000637_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/95bd02f9-c380-44d6-ad0b-19e065990546) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000637/draft/files?location=sub-BH460%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/95bd02f9-c380-44d6-ad0b-19e065990546/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 1.01 MB | 
[File info](https://api.dandiarchive.org/api/assets/cb9c155d-17a8-4c36-901f-5773735eb3d3) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000637/draft/files?location=sub-BH457%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/cb9c155d-17a8-4c36-901f-5773735eb3d3/download/) 
---

<a id="000638">*[DANDI:000638](https://dandiarchive.org/dandiset/000638/draft)*: **Hippocampus/Entorhinal Cortex Dual Region Silicon Probe recording**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Feng, (Susie) Yu (2023) Hippocampus/Entorhinal Cortex Dual Region Silicon Probe recording*

---

<a id="000639">*[DANDI:000639](https://dandiarchive.org/dandiset/000639/draft)*: **test my dandiset 1**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Boivin, Bruno (2023) test my dandiset 1*

---

<a id="000640">*[DANDI:000640](https://dandiarchive.org/dandiset/000640/draft)*: **32-CH Local Field Potential Data During Probabilistic Reversal Learning Task**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **339**, total size (MB): **30,511.57**

- Species: **Rattus norvegicus - Norway rat**

- Keywords: **electrophysiology**, **rodent behavior**, **reversal learning**, **traumatic brain injury**

- Variables measured: 

- Source paper: *Koloski, Miranda ; Ramanathan, Dhakshin (2023) 32-CH Local Field Potential Data During Probabilistic Reversal Learning Task*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000640_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/48b3edb1-d70f-4cba-9c0f-e601dd0d2d88) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000640/draft/files?location=sub-199%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/48b3edb1-d70f-4cba-9c0f-e601dd0d2d88/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/f2af98a7-41cf-4b8b-b53d-e2affb10118a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000640/draft/files?location=sub-201%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/f2af98a7-41cf-4b8b-b53d-e2affb10118a/download/) 
---

<a id="000673">*[DANDI:000673](https://dandiarchive.org/dandiset/000673/draft)*: **Data for: Control of working memory maintenance by theta-gamma phase amplitude coupling of human hippocampal neurons**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **44**, total size (MB): **23,447.04**

- Species: **Homo sapiens - Human**

- Keywords: **cognitive neuroscience**, **data standardization**, **working memory**, **neurophysiology**, **neurosurgery**, **NWB**, **open source**, **single-neurons**, **phase-amplitude coupling**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**, **Units**

- Source paper: *Daume, Jonathan; Kaminski, Jan; Schjetnan, Andrea G. P. ; Salimpour, Yousef; Khan, Umais; Kyzar, Michael; Reed, Chrystal M.; Anderson, William S.; Valiante, Taufik A.; Mamelak, Adam N.; Rutishauser, Ueli (2024) Data for: Control of working memory maintenance by theta-gamma phase amplitude coupling of human hippocampal neurons*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000673_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 191.2 MB | 
[File info](https://api.dandiarchive.org/api/assets/651572c0-b12b-491c-982a-16d60ea8f450) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000673/draft/files?location=sub-36%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/651572c0-b12b-491c-982a-16d60ea8f450/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 220.04 MB | 
[File info](https://api.dandiarchive.org/api/assets/03ce5816-3cfb-4d91-b588-b71a948c77d2) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000673/draft/files?location=sub-20%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/03ce5816-3cfb-4d91-b588-b71a948c77d2/download/) 
---

<a id="000674">*[DANDI:000674](https://dandiarchive.org/dandiset/000674/draft)*: **Volumetric multiplex imaging of whole human and non-human primate brains**</a>

, file count: **9**, total size (MB): **4,618.49**

- Variables measured: 

- Source paper: *Marx, Slayton (2023) Volumetric multiplex imaging of whole human and non-human primate brains*

---

<a id="000676">*[DANDI:000676](https://dandiarchive.org/dandiset/000676/draft)*: **Exploring zebra finch neural activity using Neuropixel Probes**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Kassahun, Ruth  (2023) Exploring zebra finch neural activity using Neuropixel Probes*

---

<a id="000677">*[DANDI:000677](https://dandiarchive.org/dandiset/000677/draft)*: **Utricular hair cell recordings from mice with constitutive knockout of K+ channel subunit Kv1.8 and wildtype/heterozygous littermates**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Martin, Hannah (2023) Utricular hair cell recordings from mice with constitutive knockout of K+ channel subunit Kv1.8 and wildtype/heterozygous littermates*

---

<a id="000678">*[DANDI:000678](https://dandiarchive.org/dandiset/000678/draft)*: **Pupil and movement measurements during mouse auditory and visual discrimination**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.2.5**), file count: **391**, total size (MB): **8,108.31**

- Species: **Mus musculus - House mouse**

- Variables measured: 

- Source paper: *Hulsey, Daniel; Zumwalt, Kevin; Mazzucato, Luca; McCormick, David A.; Jaramillo, Santiago (2023) Pupil and movement measurements during mouse auditory and visual discrimination*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000678_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 5.51 MB | 
[File info](https://api.dandiarchive.org/api/assets/4a0482ec-e9ad-41cc-a2fa-e65c6e0e0de9) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000678/draft/files?location=sub-BW053%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4a0482ec-e9ad-41cc-a2fa-e65c6e0e0de9/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 5.53 MB | 
[File info](https://api.dandiarchive.org/api/assets/b2e2aa29-b4a0-4f83-8047-1f317df31b65) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000678/draft/files?location=sub-BW051%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b2e2aa29-b4a0-4f83-8047-1f317df31b65/download/) 
---

<a id="000679">*[DANDI:000679](https://dandiarchive.org/dandiset/000679/draft)*: **Oxytocin receptors on human dorsal root and trigeminal ganglia neurons**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Yeomans, David (2023) Oxytocin receptors on human dorsal root and trigeminal ganglia neurons*

---

<a id="000680">*[DANDI:000680](https://dandiarchive.org/dandiset/000680/draft)*: **Whole brain spontaneous activity plus NeuroPAL images of semi-restricted worms**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Kimura, Kotaro (2023) Whole brain spontaneous activity plus NeuroPAL images of semi-restricted worms*

---

<a id="000682">*[DANDI:000682](https://dandiarchive.org/dandiset/000682/draft)*: **Hippocampal Interneuronal Dysfunction and Hyperexcitability in a Porcine Model of Concussion**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Wolf, John (2023) Hippocampal Interneuronal Dysfunction and Hyperexcitability in a Porcine Model of Concussion*

---

<a id="000683">*[DANDI:000683](https://dandiarchive.org/dandiset/000683/draft)*: **Element Calcium Imaging Data Upload**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **1**, total size (MB): **31.73**

- Species: **Mus musculus - House mouse**

- Variables measured: **PlaneSegmentation**, **OpticalChannel**, **ProcessingModule**, **ImagingPlane**

- Source paper: *Bakshi, Kushal (2023) Element Calcium Imaging Data Upload*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000683_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 31.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/a2dc6e4e-ab5e-4162-a76c-b53526ea4075) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000683/draft/files?location=sub-subject1%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/a2dc6e4e-ab5e-4162-a76c-b53526ea4075/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NI**  
---

<a id="000686">*[DANDI:000686](https://dandiarchive.org/dandiset/000686/draft)*: **Focusing electroporation to the center of a quadrupole electrode array by interference of unipolar pulses (NextGeneration-CANCAN)**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **11**, total size (MB): **7,252.54**

- Species: **Bos taurus - Cattle**

- Variables measured: 

- Source paper: *Silkuniene, Giedre; Pakhomov, Andrei; Gudvangen, Emily; Mangalanathan, Uma; Semenov, Iurii (2024) Focusing electroporation to the center of a quadrupole electrode array by interference of unipolar pulses (NextGeneration-CANCAN)*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL](000686_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 606.67 MB | 
[File info](https://api.dandiarchive.org/api/assets/49a72f13-107e-4d02-b163-4a9509e6c59b) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000686/draft/files?location=sub-1p-x4-10cycles-CC-600ns-200ms-6-4kV-(dish6)%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/49a72f13-107e-4d02-b163-4a9509e6c59b/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 607.71 MB | 
[File info](https://api.dandiarchive.org/api/assets/dade1a19-48f1-45ff-b6ff-f68dd4650f5f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000686/draft/files?location=sub-1p-x4-10cycles-CC-600ns-200ms-6-4kV-(dish2-2)%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/dade1a19-48f1-45ff-b6ff-f68dd4650f5f/download/) 
---

<a id="000687">*[DANDI:000687](https://dandiarchive.org/dandiset/000687/draft)*: **similarity-weighted interleaved learning**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **9**, total size (MB): **3,431,932.75**

- Species: **Mus musculus - House mouse**

- Keywords: **cortex layers**, **hippocampus**, **learning **, **memory**, **memory replay**, **memory consolidation**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Saxena, Rajat; Shobe, Justin; McNaughton, Bruce (2023) similarity-weighted interleaved learning*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000688">*[DANDI:000688](https://dandiarchive.org/dandiset/000688/draft)*: **Long-term recordings of motor and premotor cortical spiking activity during reaching in monkeys**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Perich, Matthew G.; Miller, Lee E.; Azabou, Mehdi; Dyer, Eva L. (2023) Long-term recordings of motor and premotor cortical spiking activity during reaching in monkeys*

---

<a id="000689">*[DANDI:000689](https://dandiarchive.org/dandiset/000689/draft)*: **Data supporting Neurotensin orchestrates valence  assignment in the amygdala**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **in vivo electrophysiology**, **mouse**, ** Pavlovian discrimination**, **deeplabcut**, **basolateral amygdala (BLA)**, **paraventricular nucleus of the thalamus (PVT)**, **neutotensin**, **valence assignment**

- Source paper: *Keyes, Laurel (2023) Data supporting Neurotensin orchestrates valence  assignment in the amygdala*

---

<a id="000691">*[DANDI:000691](https://dandiarchive.org/dandiset/000691/draft)*: **An optical design enabling lightweight and large field-of-view head-mounted microscopes**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **2**, total size (MB): **15,338.09**

- Species: **Mus musculus - House mouse**

- Variables measured: **TwoPhotonSeries**, **ImagingPlane**, **ProcessingModule**, **PlaneSegmentation**, **OpticalChannel**

- Source paper: *Scherrer, Joseph R.; Lynch, Galen F.; Zhang, Jie J.; Fee, Michale S. (2023) An optical design enabling lightweight and large field-of-view head-mounted microscopes*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000692">*[DANDI:000692](https://dandiarchive.org/dandiset/000692/draft)*: **Whole-brain spontaneous GCaMP activity with NeuroPAL cell ID information of semi-restricted worms**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **9**, total size (MB): **80,536.8**

- Species: **Caenorhabditis elegans**

- Variables measured: **ProcessingModule**, **PlaneSegmentation**

- Source paper: *Suzuki, Ryoga; Wen, Chentao; Sprague, Daniel; Onami, Shuichi; Kimura, Koutarou D (2023) Whole-brain spontaneous GCaMP activity with NeuroPAL cell ID information of semi-restricted worms*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000693">*[DANDI:000693](https://dandiarchive.org/dandiset/000693/draft)*: **Characterizing the effect of environmental enrichment on representational complexity and functional synaptic connectivity**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **memory consolidation**, **cognitive reserve**, **environmental enrichment**, **learning**, **schema**, **cortex layers**

- Source paper: *Saxena, Rajat; Shobe, Justin; McNaughton, Bruce; National Institute of Health (BRAIN) (2023) Characterizing the effect of environmental enrichment on representational complexity and functional synaptic connectivity*

---

<a id="000694">*[DANDI:000694](https://dandiarchive.org/dandiset/000694/draft)*: **Brainstem recordings**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *De Preter, Caitlynn (2023) Brainstem recordings*

---

<a id="000695">*[DANDI:000695](https://dandiarchive.org/dandiset/000695/draft)*: **Circadian regulation of dopamine 1 receptor signaling in the Nucleus Accumbens**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **Circadian rhythms, kcnq, excitability, medium spiny neuron, spiny projection neuron, dopamine, ventral tegmental area**

- Source paper: *Francis , Chase (2023) Circadian regulation of dopamine 1 receptor signaling in the Nucleus Accumbens*

---

<a id="000696">*[DANDI:000696](https://dandiarchive.org/dandiset/000696/draft)*: **The organization of context versus content coding in the hippocampus and neocortex**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **5**, total size (MB): **3,849,974.84**

- Species: **Mus musculus - House mouse**

- Variables measured: **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Ning, Wing (2023) The organization of context versus content coding in the hippocampus and neocortex*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000710">*[DANDI:000710](https://dandiarchive.org/dandiset/000710/draft)*: **Laminar coding properties of visual object representations in the mouse neocortex across multiple contexts**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **4**, total size (MB): **2,196,510.95**

- Species: **Mus musculus - House mouse**

- Variables measured: **ElectricalSeries**, **ElectrodeGroup**

- Source paper: *Shobe, Justin (2023) Laminar coding properties of visual object representations in the mouse neocortex across multiple contexts*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000711">*[DANDI:000711](https://dandiarchive.org/dandiset/000711/draft)*: **Allen Institute - Visual Behavior - Optical Physiology**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **6015**, total size (MB): **1,508,058.15**

- Species: **Mus musculus - House mouse**

- Keywords: **mouse**, **visual cortex**, **2-photon microscopy**, **calcium imaging**, **excitatory neurons**, **inhibitory neurons**, **novelty**, **task engagement**, **behavior**, **learning**, **change detection**, **disinhibition **

- Variables measured: **ProcessingModule**, **ImagingPlane**, **PlaneSegmentation**, **OpticalChannel**

- Source paper: *Allen Institute for Brain Science; Olsen, Shawn; Garrett, Marina; Groblewski, Peter (2023) Allen Institute - Visual Behavior - Optical Physiology*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000711_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 51.03 MB | 
[File info](https://api.dandiarchive.org/api/assets/b1bb596f-6980-4393-9be5-b7fb6098587a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000711/draft/files?location=sub-498972%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/b1bb596f-6980-4393-9be5-b7fb6098587a/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 51.56 MB | 
[File info](https://api.dandiarchive.org/api/assets/ade7fe9e-2c70-4351-b5ce-65eb767bd990) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000711/draft/files?location=sub-412036%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ade7fe9e-2c70-4351-b5ce-65eb767bd990/download/) 
---

<a id="000712">*[DANDI:000712](https://dandiarchive.org/dandiset/000712/draft)*: **test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Amin, Jai (2023) test*

---

<a id="000713">*[DANDI:000713](https://dandiarchive.org/dandiset/000713/draft)*: **Allen Institute - Visual Behavior - Neuropixels**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **4288**, total size (MB): **4,747,842.51**

- Species: **Mus musculus - House mouse**

- Variables measured: **ProcessingModule**, **ElectricalSeries**, **LFP**, **Units**

- Source paper: *Allen Institute - Visual Behavior - Neuropixels (2023).*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [CRITICAL, BEST_PRACTICE_VIOLATION](000713_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 51.42 MB | 
[File info](https://api.dandiarchive.org/api/assets/6affb667-753b-447a-b83a-3f5e4447a6f0) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000713/draft/files?location=sub-524926%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/6affb667-753b-447a-b83a-3f5e4447a6f0/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 51.42 MB | 
[File info](https://api.dandiarchive.org/api/assets/7ca1f528-413d-4ee0-a67b-1a02fb01deca) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000713/draft/files?location=sub-550324%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7ca1f528-413d-4ee0-a67b-1a02fb01deca/download/) 
---

<a id="000714">*[DANDI:000714](https://dandiarchive.org/dandiset/000714/draft)*: **Segmented and labeled NeuroPAL structural images**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **9**, total size (MB): **478.08**

- Species: **Caenorhabditis elegans**

- Variables measured: **ProcessingModule**, **PlaneSegmentation**

- Source paper: *Sprague, Daniel; Chaudhary, Shivesh; Lee, Sol Ah; Li, Yueyi; Patel, Dhaval S; Lu, Hang (2023) Segmented and labeled NeuroPAL structural images*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000714_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-0**  
   Size: 50.92 MB | 
[File info](https://api.dandiarchive.org/api/assets/4cb34249-316f-413b-9e69-1356ba09097d) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000714/draft/files?location=sub-7%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/4cb34249-316f-413b-9e69-1356ba09097d/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-0**  
   Size: 50.93 MB | 
[File info](https://api.dandiarchive.org/api/assets/eb250ec0-ff30-45f2-a328-674a872251f6) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000714/draft/files?location=sub-9%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/eb250ec0-ff30-45f2-a328-674a872251f6/download/) 
---

<a id="000715">*[DANDI:000715](https://dandiarchive.org/dandiset/000715/draft)*: **NeuroPAL: Atlas of C. elegans neuron locations and colors in NeuroPAL worm**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **10**, total size (MB): **835.04**

- Species: **Caenorhabditis elegans**

- Variables measured: **PlaneSegmentation**, **ProcessingModule**

- Source paper: *Sprague, Daniel; Eviatar Yemini (2023) NeuroPAL: Atlas of C. elegans neuron locations and colors in NeuroPAL worm*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [ERROR](000715_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-0**  
   Size: 70.95 MB | 
[File info](https://api.dandiarchive.org/api/assets/c5fdc4db-0942-4856-98a9-4ed96fc47faa) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000715/draft/files?location=sub-76-YAaDV%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c5fdc4db-0942-4856-98a9-4ed96fc47faa/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-0**  
   Size: 71.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/ab614422-ae5f-4111-b2c9-f7199d7c3cb8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000715/draft/files?location=sub-70-YAaLR%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ab614422-ae5f-4111-b2c9-f7199d7c3cb8/download/) 
---

<a id="000716">*[DANDI:000716](https://dandiarchive.org/dandiset/000716/draft)*: **Peristimulus Time Histograms Derived from Electrophysiological Recordings in the Inferotemporal Cortex of Macaques During RSVP Tasks**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *ABLITIP, ALIYA (2023) Peristimulus Time Histograms Derived from Electrophysiological Recordings in the Inferotemporal Cortex of Macaques During RSVP Tasks*

---

<a id="000717">*[DANDI:000717](https://dandiarchive.org/dandiset/000717/draft)*: **CatalystNeuro Placeholder 1**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Flynn, Garrett (2023) CatalystNeuro Placeholder 1*

---

<a id="000718">*[DANDI:000718](https://dandiarchive.org/dandiset/000718/draft)*: **CatalystNeuro Placeholder 2**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Flynn, Garrett (2023) CatalystNeuro Placeholder 2*

---

<a id="000719">*[DANDI:000719](https://dandiarchive.org/dandiset/000719/draft)*: **CatalystNeuro Placeholder 3**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Flynn, Garrett (2023) CatalystNeuro Placeholder 3*

---

<a id="000722">*[DANDI:000722](https://dandiarchive.org/dandiset/000722/draft)*: **UNet Validation Data**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Chollet, Etienne (2023) UNet Validation Data*

---

<a id="000723">*[DANDI:000723](https://dandiarchive.org/dandiset/000723/draft)*: **VR-SASE Virtual Reality Dendritic Spine Analysis**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Reimer, Marike (2023) VR-SASE Virtual Reality Dendritic Spine Analysis*

---

<a id="000724">*[DANDI:000724](https://dandiarchive.org/dandiset/000724/draft)*: **Multimodal Human Brain Imaging Data**</a>

- Data type: **Brain Imaging Data Structure (BIDS)**, file count: **8**, total size (MB): **1,890.34**

- Variables measured: 

- Source paper: *Gunalan, Kabilar (2024) Multimodal Human Brain Imaging Data*

---

<a id="000726">*[DANDI:000726](https://dandiarchive.org/dandiset/000726/draft)*: **4chDemoPL2.pl2**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Hussein, Kareem (2023) 4chDemoPL2.pl2*

---

<a id="000727">*[DANDI:000727](https://dandiarchive.org/dandiset/000727/draft)*: **Mapping the Neural Dynamics of Locomotion across the Drosophila Brain**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **18**, total size (MB): **609,568.5**

- Species: **Drosophila melanogaster - Fruit fly**

- Variables measured: **OpticalChannel**, **ImagingPlane**, **Position**, **ProcessingModule**, **TwoPhotonSeries**, **SpatialSeries**

- Source paper: *Brezovec, Luke; Berger, Andrew; Druckmann, Shaul ; Clandinin, Thomas (2024) Mapping the Neural Dynamics of Locomotion across the Drosophila Brain*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000728">*[DANDI:000728](https://dandiarchive.org/dandiset/000728/draft)*: **Allen Institute - Visual Coding - Optical Physiology**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **1103**, total size (MB): **378,236.14**

- Species: **Mus musculus - House mouse**

- Variables measured: **PlaneSegmentation**, **BehavioralTimeSeries**, **ImagingPlane**, **ProcessingModule**, **OpticalChannel**

- Source paper: *Baker, Cody (2023) Allen Institute - Visual Coding - Optical Physiology*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [BEST_PRACTICE_VIOLATION](000728_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 117.33 MB | 
[File info](https://api.dandiarchive.org/api/assets/cfde80fc-9864-4a8b-9fe8-ba6728a29f92) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000728/draft/files?location=sub-644572921%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/cfde80fc-9864-4a8b-9fe8-ba6728a29f92/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 119.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/c0707671-5a7b-4abe-8447-3e5ef4965ec8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000728/draft/files?location=sub-570077427%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/c0707671-5a7b-4abe-8447-3e5ef4965ec8/download/) 
---

<a id="000730">*[DANDI:000730](https://dandiarchive.org/dandiset/000730/draft)*: **General data test**</a>

, file count: **0**, total size (MB): **0.0**

- Keywords: **general**

- Source paper: *Platholi, Jimcy (2023) General data test*

---

<a id="000732">*[DANDI:000732](https://dandiarchive.org/dandiset/000732/draft)*: **Protosequences in human cortical organoids model intrinsic states in the developing cortex**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **36**, total size (MB): **112,811.77**

- Species: **Homo sapiens - Human**

- Variables measured: **Units**, **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Molen, Tjitse van der; Spaeth, Alex; Chini, Mattia; Bartram, Julian; Dendukuri, Adi; Zhang, Zongren; Bhaskaran-Nair, Kiran; Petzold, Linda R.; Hansma, Paul K.; Teodorescu, Mircea; Hierlemann, Andreas; Hengen, Keith B.; Hanganu-Opatz, Ileana L.; Kosik, Kenneth S.; Blauvelt, Lon; Sharf, Tal (2023) Protosequences in human cortical organoids model intrinsic states in the developing cortex*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000732_validation.txt) 

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 1: **LL-V**  
   Size: 0.24 MB | 
[File info](https://api.dandiarchive.org/api/assets/ac632a6f-17d2-45e0-ab58-d56837290b85) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000732/draft/files?location=sub-U%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/ac632a6f-17d2-45e0-ab58-d56837290b85/download/) 
- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) NWBE compatibility - example file 2: **LL-V**  
   Size: 0.28 MB | 
[File info](https://api.dandiarchive.org/api/assets/e46da05c-611f-4074-9f75-fc0a44d1e6be) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000732/draft/files?location=sub-U%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/e46da05c-611f-4074-9f75-fc0a44d1e6be/download/) 
---

<a id="000733">*[DANDI:000733](https://dandiarchive.org/dandiset/000733/draft)*: **h5ad test**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Jarecka, Dorota (2023) h5ad test*

---

<a id="000766">*[DANDI:000766](https://dandiarchive.org/dandiset/000766/draft)*: **Novel genetically encoded tools for imaging or silencing neuropeptide release from presynaptic terminals in vivo**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Kim , Dongil (2023) Novel genetically encoded tools for imaging or silencing neuropeptide release from presynaptic terminals in vivo*

---

<a id="000768">*[DANDI:000768](https://dandiarchive.org/dandiset/000768/draft)*: **20231222_AIBS_Patchseq_nonhuman_primate**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **51**, total size (MB): **3,153.3**

- Species: **Macaca nemestrina**

- Keywords: **Patch-seq**, **non-human primate**, **multimodal**

- Variables measured: **CurrentClampStimulusSeries**, **CurrentClampSeries**, **ProcessingModule**, **VoltageClampStimulusSeries**, **VoltageClampSeries**

- Source paper: *Soliman, Sherif; Lee, Brian; National Institute of Mental Health; Kalmbach, Brian; Dalley, Rachel; Lein, Ed (2023) 20231222_AIBS_Patchseq_nonhuman_primate*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000768_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 41.21 MB | 
[File info](https://api.dandiarchive.org/api/assets/7d2103a6-6e32-4956-88f6-1fb4b51a9441) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000768/draft/files?location=sub-1288510508%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7d2103a6-6e32-4956-88f6-1fb4b51a9441/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 44.12 MB | 
[File info](https://api.dandiarchive.org/api/assets/8cb4a324-55c5-4451-ab93-ea6994553fba) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000768/draft/files?location=sub-1285385365%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/8cb4a324-55c5-4451-ab93-ea6994553fba/download/) 
---

<a id="000769">*[DANDI:000769](https://dandiarchive.org/dandiset/000769/draft)*: **20231222_AIBS_Patchseq_human**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.3.0**), file count: **177**, total size (MB): **10,299.06**

- Species: **Homo sapiens - Human**

- Keywords: **Patch-seq**, **human**, **multimodal**

- Variables measured: **CurrentClampStimulusSeries**, **VoltageClampSeries**, **VoltageClampStimulusSeries**, **ProcessingModule**, **CurrentClampSeries**

- Source paper: *Soliman, Sherif; Lee, Brian; Allen Institute for Brian Science; National Institute of Mental Health; Kalmbach, Brian; Dalley, Rachel; Lein, Ed (2023) 20231222_AIBS_Patchseq_human*

- ![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png) Validation results summary: [PYNWB_VALIDATION, BEST_PRACTICE_VIOLATION](000769_validation.txt) 

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 1: **LL-P**  
   Size: 23.63 MB | 
[File info](https://api.dandiarchive.org/api/assets/7b5348c1-4b25-41f3-ab48-5301851cc2b8) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000769/draft/files?location=sub-1269274954%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/7b5348c1-4b25-41f3-ab48-5301851cc2b8/download/) 
- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) NWBE compatibility - example file 2: **LL-P**  
   Size: 25.68 MB | 
[File info](https://api.dandiarchive.org/api/assets/29e6a714-e15f-43c4-a138-3e5b55532626) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000769/draft/files?location=sub-1260690332%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/29e6a714-e15f-43c4-a138-3e5b55532626/download/) 
---

<a id="000776">*[DANDI:000776](https://dandiarchive.org/dandiset/000776/draft)*: **Brain-wide representations of behavior spanning multiple timescales and states in C. elegans**</a>

- Data type: **Neurodata Without Borders (NWB)**, file count: **38**, total size (MB): **1,045,238.28**

- Species: **Caenorhabditis elegans**

- Variables measured: **PlaneSegmentation**, **BehavioralEvents**, **BehavioralTimeSeries**, **ProcessingModule**

- Source paper: *Sprague, Daniel (2024) Brain-wide representations of behavior spanning multiple timescales and states in C. elegans*

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: NULL_FILE_LIMIT

---

<a id="000783">*[DANDI:000783](https://dandiarchive.org/dandiset/000783/draft)*: **test-zarr**</a>

, file count: **1**, total size (MB): **0.0**

- Source paper: *Kanzer, Aaron (2024) test-zarr*

---

<a id="000784">*[DANDI:000784](https://dandiarchive.org/dandiset/000784/draft)*: **vector compositionality Jazayeri Lab**</a>

- Data type: **Neurodata Without Borders (NWB)** (**version 2.6.0**), file count: **5**, total size (MB): **261,081.37**

- Species: **Macaca mulatta - Rhesus monkey**

- Variables measured: **Units**, **ProcessingModule**, **ElectrodeGroup**, **ElectricalSeries**

- Source paper: *Tang, Cheng (2024) vector compositionality Jazayeri Lab*

- ![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png) Validation results summary: [PASSED_VALIDATION](000784_validation.txt) 

- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 1: **NC-1**  
   Size: 240.73 MB | 
[File info](https://api.dandiarchive.org/api/assets/1eb689ce-e1f1-4717-8074-03ee50e6d70a) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000784/draft/files?location=sub-F%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/1eb689ce-e1f1-4717-8074-03ee50e6d70a/download/) 
- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) NWBE compatibility - example file 2: **NC-1**  
   Size: 519.17 MB | 
[File info](https://api.dandiarchive.org/api/assets/d582b54f-f593-4dd0-a901-a1dac2513f6f) | 
[View on DANDI Web](https://dandiarchive.org/dandiset/000784/draft/files?location=sub-F%2F) | 
[View on NWB Explorer](http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/d582b54f-f593-4dd0-a901-a1dac2513f6f/download/) 
---

<a id="000872">*[DANDI:000872](https://dandiarchive.org/dandiset/000872/draft)*: **Glymphatic Fluid Transport Is Suppressed by the AQP4 Inhibitor AER-271**</a>

, file count: **0**, total size (MB): **0.0**

- Source paper: *Giannetto, Michael J.; Gomolka, Ryszard S. (2024) Glymphatic Fluid Transport Is Suppressed by the AQP4 Inhibitor AER-271*

---

</p></details>