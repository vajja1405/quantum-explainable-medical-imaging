[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NpNf3mgTx0-4_shmHh0PwvejUEFMEO8I?usp=sharing)


# Explainable and Quantum AI for Medical Imaging Systems

Graduate Research – University of Missouri–Kansas City  
Advisor: Prof. Luke Miller  
Duration: Aug 2025 – Dec 2025

## Overview

This research benchmarks classical and quantum machine learning architectures on medical imaging tasks.

Models evaluated:

- CNN
- QCNN
- SVM
- QSVM

## Results

- Classical CNN achieved AUROC = 0.76
- QCNN achieved 5× faster training time compared to CNN
- Evaluation metrics: AUROC, AUCPR, F1-score

## Explainability

- SHAP for feature importance
- Grad-CAM for visual interpretability

## Contributions

- Comparative study of classical vs quantum ML
- Computational efficiency analysis
- Explainability validation across architectures


## Research Paper & Poster

📄 Research Paper: [Read Full Paper](https://drive.google.com/file/d/1ZL2x0kbnx-VQnojByAn5yibv0oKIShI2/view)
📊 Research Poster: [See Poster](https://drive.google.com/file/d/1zlh1b2yddr9GL556Hlyz37CIzbk7zkyN/view)

## Practical use and reproducibility limits

This study supports a researcher's model-selection decision: compare predictive
performance and computational cost under the same data split and compute budget.
It is not a medical diagnostic product. SHAP and Grad-CAM help inspect patterns;
they do not validate every prediction. The reported 5x training-time result lacks
local run metadata, so it should not be advertised as a general quantum advantage.

`benchmark_audit.py` now checks paired run metadata before calculating a runtime
ratio. Run `python -m unittest discover -s tests -v` offline. Its test fixtures are
synthetic software tests, not new research measurements. The original notebook
and paper remain external links; no models were retrained in this update.

A useful next experiment (not completed) records dataset/version, subject-level
splits, seeds, hardware, sample counts, epochs, wall time and AUROC/AUPRC/F1 for
each architecture, with repeated seeds and uncertainty. Inspect errors and
attributions before proposing a human-reviewed clinical study.
