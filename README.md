# Network Automation

[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/)
[![Netmiko](https://img.shields.io/pypi/v/netmiko.svg)](https://pypi.org/project/netmiko/)


## Overview : 

This project focuses on automating network operations by implementing specific solutions for Cisco devices. Currently, we utilize Python libraries such as Netmiko, Paramiko, and NAPALM to connect, configure, and manage Cisco equipment efficiently and consistently. However, it is worth noting that additional libraries may be explored in the future to address specific needs or leverage new technological advancements in the field of network automation.

The primary goal is to enhance operational efficiency and reduce human errors associated with manual configuration and management of network devices. Automation also enables increased scalability and centralized management of network infrastructures, contributing to the modernization and optimization of computer networks.

This project is scalable, and regular updates will be made to existing scripts as it progresses. Future enhancements will include adding additional features, optimizing code, and integrating new libraries and automation techniques.

Ultimately, the ultimate goal is to create a web-based network monitoring platform that leverages existing automation scripts. This platform will provide a user-friendly interface for monitoring and managing network devices, offering real-time operational data, alerts, and detailed reports to facilitate decision-making and performance optimization of network infrastructure.

## Getting Started

### Features

- Establish SSH connections to Cisco devices
- Configure and manage Cisco devices using Python scripts
- Automate network operations encompassing provisioning, configuration adjustments, and data collection
- Scalable and adaptable for future enhancements

### Requirements

#### Environment Setup:

1. **GNS3:**
   - Download and install GNS3 from the official website: [https://www.gns3.com/](https://www.gns3.com/)
   - Follow the installation instructions specific to your operating system.

2. **VMware Workstation:**
   - Download and install VMware Workstation from the official website: [https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html)
   - Follow the installation instructions specific to your operating system.

3. **GNS3 and VMware Workstation Setup:**
   - Launch GNS3 and configure it to work with VMware Workstation as outlined in the GNS3 documentation.

4. **Cisco IOS Image:**
   - Obtain a valid Cisco IOS image from authorized sources, ensuring you have the necessary licenses for testing purposes.

5. **Python Dependencies:**
   - Install the required dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```
     Use this code with caution.

*Note: The installation instructions provided are most relevant to users setting up a development environment for network automation using GNS3 and Cisco IOS images. If you're solely using pre-existing scripts for Cisco automation without GNS3, these steps might not be necessary.*

## Contribution

We welcome contributions from the community! If you have any ideas or improvements for this project, feel free to open a pull request. Here are some helpful guidelines:

1. **Fork the Repository:**
   - Visit this project's GitHub repository and click the "Fork" button to create your own copy on GitHub.

2. **Clone Your Fork:**
   - Open a terminal or command prompt and use the `git clone` command to clone your forked repository to your local machine. Replace `<username>` with your GitHub username:
     ```bash
     git clone https://github.com/<username>/<repository-name>.git
     ```
     Use this code with caution.

3. **Create a New Branch:**
   - Navigate to your local repository directory using the `cd` command.
   - Create a new branch for your specific contributions using the `git checkout` command, followed by a descriptive branch name:
     ```bash
     cd <repository-name>
     git checkout -b <branch-name>
     ```
     Use this code with caution.

4. **Make Your Changes:**
   - Make the desired modifications to the code and documentation. It's crucial to follow good coding practices and document your changes clearly.

5. **Test Your Changes:**
   - Thoroughly test your modifications to ensure they don't introduce regressions or break existing functionality.

6. **Commit Your Changes:**
   - Stage your changes using the `git add` command, followed by a clear and concise commit message using `git commit`:
     ```bash
     git add .
     git commit -m "Your informative commit message"
     ```
     Use this code with caution.

7. **Push Your Changes:**
   - Push your committed changes to your forked repository on GitHub using the `git push` command:
     ```bash
     git push origin <branch-name>
     ```
     Use this code with caution.

8. **Open a Pull Request:**
   - On GitHub, navigate to your forked repository and click the "Pull requests" tab.
   - Click the "New pull request" button and select the branch containing your changes to create a pull request.
   - Provide a clear and detailed description of your contributions in the pull request description.

We appreciate your willingness to contribute to this project!


# License

This project is licensed under the MIT License.

# Contributors

- **NEGGAZI Mohamed Chakib**
- **TADRIST Zakaria**
  

