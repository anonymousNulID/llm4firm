# FirmLLM - A Large Language Model-based Multi-Agent System for Large-scale Firmware Collection and Analysis

FirmLLM is an integrated system that combines firmware collection and analysis functions, leveraging large language models (LLM) for intelligent firmware analysis. The system consists of two core modules: the firmware collection system (FirmCrawler) and the firmware analysis system (FirmAnalyzer). Both systems adopt a multi-agent collaborative approach based on user-defined prompts, enabling autonomous exploration and analysis, and can solve long-cycle complex tasks.


## Project Structure

```
.
├── firmcrawler/       # Firmware Collection System
├── firmanalyzer/      # Firmware Analysis System
└── Examples/   # Analysis Result Samples
```

## System Components

### 1. Firmware Collection System (FirmCrawler)

`firmcrawler` is used for automated collection of firmware files from various manufacturers. The system is built upon and optimized from [WebVoyager](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/) [[paper]](https://arxiv.org/abs/2401.13919), implementing a multi-agent collaboration system for large-scale firmware collection. WebVoyager is an innovative Large Multimodal Model (LMM) powered web agent that can complete user instructions end-to-end by interacting with real-world websites.

#### Vendor URL
- D-Link: `https://support.dlink.com/AllPro.aspx`
- Foscam: `https://www.foscam.com/download-center/firmware-downloads.html`
- Mercury: `http://service.mercurycom.com.cn/download-list.html`
- MikroTik: `https://www.mikrotik.com/download`
- OpenWrt: `https://downloads.openwrt.org/releases/`
- QNAP: `https://www.qnap.com/en/download/`
- Supermicro: `https://www.supermicro.com/zh_cn/products/motherboards/embedded-iot-boards`
- TP-Link:
  - English: `https://www.tp-link.com/hk/support/download/`
  - Chinese: `https://resource.tp-link.com.cn/?productorlist=0`
- UI: `https://www.ui.com/download/releases/firmware`
- Zyxel: `https://www.zyxel.com/global/en/products`

#### Main Features
- Automated web interaction and downloads
- Intelligent firmware information collection
- Multi-agent collaboration for parallel crawling
- Distributed task scheduling

#### Core Files
- `crawler.py`: Core crawler implementation based on WebVoyager
- `web_intrect.py`: Web interaction module
- `mark_page.js`: Page marking script
- `prompt.yaml`: Vendor-specific customized prompts for intelligent crawling

### 2. Firmware Analysis System (FirmAnalyzer)

`firmanalyzer` provides comprehensive firmware security analysis capabilities.

#### Main Features
- Firmware unpacking and filesystem identification
- Static analysis and vulnerability detection
- Binary analysis
- CVE vulnerability matching
- Security risk assessment

#### Core Files
- `run.py`: System entry point
- `explore.py`: Firmware exploration
- `analyze.py`: Firmware file analysis
  - Shell Command Executor: Support for cat, grep, and other Linux tools
  - CVE Query Tool: Support for API interface queries
  - Disassembly Assistant: Integration with radare2 and LLM
  - Sensitive Information Pattern Matching: Code pattern recognition based on regex and semantics
- `requirements.yaml`: Analysis configuration file
  - File Requirements: Defines target file types and components for analysis
  - Directory Requirements: Specifies priority directories and analysis areas
  - Analysis Requirements: Configures security analysis workflow and severity criteria
  - Report Templates: Customizable templates for security reports and summaries

The requirements.yaml allows users to customize:
- Analysis scope and target components
- Directory scanning priorities
- Security analysis strategies
- Risk severity classifications
- Report and summary formats

#### Data Sources
- FirmSec Dataset: https://github.com/NESA-Lab/FirmSecDataset

### 3. Analysis Result Samples

`Examples` contains analysis results using DeepSeek-v3 and DeepSeek-r1 models.

#### Analysis Logs and Reports
- `explore.log`: Complete firmware analysis process example
- `report.txt`: Detailed security analysis report by file
- `summary.txt`: Overall firmware security issues summary and risk level assessment

#### Sample Firmware
- OpenWrt
- D-Link 
- MikroTik RouterOS
- Ubiquiti
## Limitations and Challenges

While FirmLLM demonstrates significant advancements in firmware analysis compared to existing tools, our approach has the following limitations:

### 1. Semantic Understanding Constraints
- **Configuration Interpretation**:  
  Traditional tools (Firmadyne, FirmWalker, EMBA) lack contextual understanding of configuration semantics. While our LLM-based approach improves this, challenges remain with:
  - Custom encryption/obfuscation implementations
  - Non-standard configuration formats without documentation
  - Potential hallucinations in configuration parsing

- **Code Analysis**:  
  Compared to static analysis tools (Binwalk, Ghidra):
  - Limited understanding of indirect function calls in binary code
  - Challenges with vendor-specific compiler optimizations
  - Requires manual verification for complex control flows

### 2. Experimental Validation Difficulties
- **Penetration Testing Constraints**:
  - Physical device requirements for vulnerability reproduction (avg. 3-7 days/firmware vs 4-8 hours analysis)
  - Network service verification demands full firmware emulation
  - Limited ground truth data for IoT vulnerability benchmarks

- **Tool Comparison Limitations**:
  - No direct apples-to-apples comparison possible due to:
  - Fundamental architectural differences (LLM vs. static analysis)
  - Varied vulnerability detection methodologies
  - Lack of standardized firmware security benchmarks

### 3. Temporal and Technical Constraints
- **System Limitations**:
  - Model API rate limits (deepseek) restrict throughput
  - Hardware dependencies for specific vendor validation
  - CVE matching latency (24-72h update cycle for NVD database)

- **Scope Boundaries**:
  - Excludes low-level hardware interaction analysis
  - Limited to firmware packages <2GB due to memory constraints
  - Web interface analysis currently supports 85% of common CMS frameworks

These challenges highlight three fundamental tensions in firmware analysis:  
1) **Comprehensiveness vs. Precision**: Full semantic understanding requires impractical computational resources  
2) **Automation vs. Verification**: LLM-generated findings need human-in-the-loop validation  
3) **Timeliness vs. Accuracy**: Rapid analysis trades off with vulnerability confirmation  

Our roadmap prioritizes hybrid approaches combining:  
- Symbolic execution for critical path verification  
- Differential analysis across firmware versions  
- Hardware-assisted validation frameworks
## Notes

1. Analysis results are for research reference only
2. Please comply with relevant laws and regulations
3. Verification in test environment is recommended
