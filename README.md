# FirmLLM

A Multi-Agent System for Large-Scale Firmware Collection and Analysis Based on Large Language Models

FirmLLM is designed to **automate long-cycle analysis tasks** by leveraging multi-agent collaboration and LLMs, enabling scalable and intelligent firmware collection and vulnerability analysis.


---

## Overview

**FirmLLM** is an integrated system for large-scale firmware acquisition and security analysis. It leverages multi-agent collaboration and large language models (LLMs) to achieve intelligent automation in both crawling and analysis.

The system consists of two main modules:

- **FirmCrawler**: A multi-agent web crawler for automated firmware collection  
- **FirmAnalyzer**: A firmware security analysis engine that combines static tools and LLM capabilities

---

## 📁 Project Structure

```
.
├── firmcrawler/       # Firmware Collection System
├── firmanalyzer/      # Firmware Analysis System
└── Examples/   # Analysis Result Samples
```


---

## 🕸️ Firmware Collection System (FirmCrawler)

Based on [WebVoyager](https://langchain-ai.github.io/langgraph/tutorials/web-navigation/web_voyager/) [[paper]](https://arxiv.org/abs/2401.13919), FirmCrawler enables intelligent interaction with vendor websites to automatically locate and download firmware files.

### ✅ Supported Vendors and URLs

- **D-Link**: https://support.dlink.com/AllPro.aspx  
- **Foscam**: https://www.foscam.com/download-center/firmware-downloads.html  
- **Mercury**: http://service.mercurycom.com.cn/download-list.html  
- **MikroTik**: https://www.mikrotik.com/download  
- **OpenWrt**: https://downloads.openwrt.org/releases/  
- **QNAP**: https://www.qnap.com/en/download/  
- **Supermicro**: https://www.supermicro.com/zh_cn/products/motherboards/embedded-iot-boards  
- **TP-Link (English)**: https://www.tp-link.com/hk/support/download/  
- **TP-Link (Chinese)**: https://resource.tp-link.com.cn/?productorlist=0  
- **Ubiquiti (UI)**: https://www.ui.com/download/releases/firmware  
- **Zyxel**: https://www.zyxel.com/global/en/products  

### 🔧 Key Features

- Autonomous interaction with vendor sites  
- Intelligent firmware file identification and retrieval  
- Multi-agent concurrent crawling  
- Distributed task scheduling

### 📄 Core Files

- `crawler.py`: Core crawler logic  
- `web_intrect.py`: Web interaction controller  
- `mark_page.js`: Web element tagging script  
- `prompt.yaml`: Vendor-specific prompt configuration for LLM

---

## 🔍 Firmware Analysis System (FirmAnalyzer)

Combines conventional static analysis, symbolic execution, and LLM-based reasoning to offer in-depth firmware security evaluation.

### 🛠️ Key Capabilities

- Firmware unpacking and filesystem detection  
- Static and semantic vulnerability detection  
- Binary disassembly and logic analysis  
- CVE correlation and risk scoring  
- Human-readable reports powered by LLMs

### 📄 Core Files

- `run.py`: Entry point for analysis  
- `explore.py`: Filesystem exploration and metadata gathering  
- `analyze.py`: Firmware file analysis module  
  - **Sensitive Info Pattern Matching**: Regex and semantic pattern detection (preliminary filtering to guide LLM inspection and direction)  
  - **Shell Command Executor**: Executes Linux tools such as `cat`, `grep`, etc.  
  - **CVE Query Tool**: Queries vulnerability data through APIs  
  - **Disassembly Assistant**: Integrates `radare2` with LLM for binary reasoning

### 🔌 Data Sources

- [FirmSec Dataset](https://github.com/NESA-Lab/FirmSecDataset)

---

## 📊 Example Outputs (Examples)

Contains complete logs and reports from analyzing firmware using **DeepSeek-v3** and **DeepSeek-r1** models.

### 📝 Files

- `explore.log`: Full exploration log  
- `report.txt`: File-by-file security analysis  
- `summary.txt`: Overall security summary and risk level

### 🧪 Firmware Examples

- OpenWrt  
- D-Link  
- MikroTik RouterOS  
- Ubiquiti  

### 🤖 Model Performance Notes

We primarily use **DeepSeek-v3** and **DeepSeek-r1** for firmware analysis.  
However, our experiments have shown that **Claude-Sonnet** demonstrates promising performance in code auditing tasks, especially for semantic reasoning and cross-file logic analysis.

DeepSeek offers lower costs, but we are actively experimenting and comparing results across multiple models to find the optimal configuration.

---

## ⚠️ Limitations and Challenges

### Format & Semantic Limitations

- Inability to automatically decrypt or handle proprietary firmware formats  
- LLMs may hallucinate when analyzing complex control flows  
- Limited understanding of intricate build scripts and service configurations

### Experimental Verification Bottlenecks

- Lack of standardized firmware security benchmarks  
- Inconsistent vulnerability reporting ground truth  
- Physical device validation may take 3–5 days per firmware

### Technical Constraints

- LLM API rate limits reduce processing parallelism  
- CVE data synchronization delays due to NVD refresh cycles  
- No modeling of low-level hardware interactions

### Core Tensions in Firmware Security

1. **Comprehensiveness vs. Precision**  
2. **Automation vs. Human Validation**  
3. **Timeliness vs. Accuracy**

---

## 🚧 Roadmap

Upcoming work will focus on:

- **Integrating more static analysis tools**, especially for binary-focused workflows to improve analysis coverage and accuracy  
- **Combining symbolic execution with LLMs** to enhance deep vulnerability discovery and validation  
- **Exploring firmware runtime state analysis** (e.g., process behavior, service call graphs, and system responses) to prioritize high-risk issues

---

## 📌 Notes & Compliance

1. All results are for **research purposes only**  
2. Please ensure legal and ethical use of the system  
3. Verification should be performed in sandboxed/test environments  
4. We are actively engaging with vendors to confirm findings and, under compliant conditions, release more security reports

---
