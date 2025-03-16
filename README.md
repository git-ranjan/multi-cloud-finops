# Multi-Cloud FinOps Automation

## Overview
This project automates cost optimization and monitoring for **AWS, GCP, and Azure** using AI-powered predictions, Kubernetes auto-scaling, and Grafana dashboards.  
🚀 **New Enhancements Added!** → **AI Cost Anomaly Detection, Spot Instance Optimization, and Rightsizing Recommendations**.

## Features
### 1️⃣ AI-Powered Cost Predictions  
- Uses **Machine Learning (Linear Regression)** to predict future cloud costs.  
- Trains on historical billing data to identify trends and forecast upcoming expenses.  
- Helps finance and DevOps teams **plan budgets proactively**.  

### 2️⃣ Kubernetes Cost Optimization (KEDA Auto-Scaling)  
- Uses **KEDA (Kubernetes Event-Driven Autoscaling)** to dynamically scale workloads.  
- Prevents **over-provisioning** by adjusting replica counts based on real-time CPU usage.  
- Reduces cloud costs while ensuring performance.  

### 3️⃣ AI-Based Cost Anomaly Detection  
- Uses **Isolation Forest Algorithm** to detect unusual cloud cost spikes.  
- Flags unexpected cost anomalies in `output/cost_anomalies.csv`.  
- Helps businesses identify **billing errors and unexpected resource usage**.  

### 4️⃣ Multi-Cloud Spot Instance Optimization  
- Uses **AWS Spot Instances** to run workloads at a lower cost.  
- Requests **t3.medium** instances with real-time bidding.  
- Helps optimize compute costs while maintaining availability.  

### 5️⃣ Automated Rightsizing Recommendations  
- Uses **AWS Cost Explorer API** to recommend optimal instance sizes.  
- Identifies **over-provisioned and underutilized** cloud resources.  
- Saves optimization suggestions in `output/rightsizing_recommendations.json`.  

### 6️⃣ Customizable Grafana Dashboards  
- Provides **real-time cost visibility** for AWS, GCP, and Azure.  
- Displays per-service, per-region cost breakdowns.  
- Helps businesses make **data-driven cost decisions**.  

## Installation & Setup
1️⃣ Clone the repository:  
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/multi-cloud-finops.git
   cd multi-cloud-finops
   ```

2️⃣ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3️⃣ Train the AI model and predict future costs:  
   ```bash
   python src/ai_cost_prediction.py
   ```

4️⃣ Run AI Anomaly Detection:  
   ```bash
   python src/ai_anomaly_detection.py
   ```

5️⃣ Deploy Kubernetes Auto-Scaler:  
   ```bash
   kubectl apply -f kubernetes/keda_autoscaler.yaml
   ```

6️⃣ Optimize costs with Spot Instances:  
   ```bash
   python automation/spot_instance_optimization.py
   ```

7️⃣ Generate Automated Rightsizing Recommendations:  
   ```bash
   python automation/rightsizing_recommendations.py
   ```

8️⃣ Set up Grafana dashboard:  
   - Import `monitoring/grafana_dashboard.json` into Grafana.  
   - Connect Prometheus to fetch cloud billing metrics.  

## Real-World Applications
🔹 **IT & DevOps Teams** → Reduce cloud waste & optimize workloads.  
🔹 **Finance Departments** → Forecast future cloud costs & detect anomalies.  
🔹 **Cloud-Native Businesses** → Improve cloud governance and FinOps strategies.  

## Future Enhancements
🔹 **Advanced AI models** for anomaly detection in cloud billing.  
🔹 **Multi-cloud Spot Instance Optimization for Kubernetes workloads**.  
🔹 **Automated Rightsizing Recommendations for all cloud services**.  

---
💡 *Contribute & Improve: Fork this repo and help build the future of FinOps!* 🚀
