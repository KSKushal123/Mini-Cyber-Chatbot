import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Define a set of pairs containing patterns and responses.
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi there!", "Hello!"]),
    (r"bye|exit", ["Goodbye!", "See you later!", "Bye!"]),
    (r"what is your name",["My name is Mini Chatbot."]),
    (r"What does VPN stand for and what is its purpose",["VPN stands for Virtual Private Network, and it is used to secure internet connections by encrypting data and masking IP addresses."]),
    (r"What is malware",["Malware, short for malicious software, includes any software intentionally designed to cause damage to a computer, server, client, or computer network."]),
    (r"How does ransomware work",["Ransomware encrypts the victim's data and demands payment in exchange for the decryption key."]),
    (r"What is social engineering",["Social engineering is a manipulation technique that exploits human error to gain private information, access, or valuables."]),
    (r"What is a brute force attack",["A brute force attack is a trial-and-error method used to decode encrypted data such as passwords or Data Encryption Standard (DES) keys."]),
    (r"What is endpoint security",["Endpoint security refers to the process of securing the various endpoints on a network, often defined as end-user devices such as mobile devices, laptops, and desktop PCs."]),
    (r"What are the main differences between a virus and a worm",["A virus is malware that attaches itself to clean files and infects other clean files, while a worm is a standalone software that replicates itself to spread to other computers."]),
    (r"What is a man-in-the-middle (MitM) attack",["A man-in-the-middle attack is where an attacker secretly relays and possibly alters the communication between two parties who believe they are directly communicating with each other."]),
    (r"What is a cryptographic hash function",["A cryptographic hash function is a mathematical algorithm that converts an input into a fixed-size string of bytes, typically used for security or data integrity."]),
    (r"What is spear phishing",["Spear phishing is a targeted attempt to steal sensitive information such as account credentials or financial information from a specific individual, often by masquerading as a trustworthy entity or person in email communications."]),
    (r"What is a security audit",["A security audit is a systematic evaluation of the security of a company's information system by measuring how well it conforms to a set of established criteria."]),
    (r"what is phishing", ["Phishing is a type of cyber attack where a target is contacted by email, telephone or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data such as personally identifiable information, banking and credit card details, and passwords."]),
    (r"What is an intrusion detection system (IDS)",["An Intrusion Detection System is a device or software application that monitors a network or systems for malicious activity or policy violations."]),
    (r"What are zero-day exploits",["Zero-Day exploits are attacks that take advantage of a previously unknown vulnerability in software, before the developer has made a patch available."]),
    (r"What is a botnet",["A botnet is a network of private computers infected with malicious software and controlled as a group without the owners' knowledge, e.g., to send spam messages."]),
    (r"What is identity theft",["Identity theft is the fraudulent acquisition and use of a person's private identifying information, usually for financial gain."]),
    (r"What is a security vulnerability",["A security vulnerability is a weakness which can be exploited by a threat actor, such as an attacker, to perform unauthorized actions within a computer system."]),
    (r"What is a penetration test",["A penetration test, or pen test, is a simulated cyberattack on a computer system to evaluate its security and identify weaknesses."]),
    (r"What is a security patch",["A security patch is a software update designed to fix vulnerabilities or improve security in a system or application."]),
    (r"What is a security incident",["A security incident is any event that compromises the confidentiality, integrity, or availability of information or systems."]),
    (r"What is a data breach",[" A data breach is an incident where sensitive, protected, or confidential information is accessed or disclosed without authorization."]),
    (r"What is cybersecurity awareness training",["Cybersecurity awareness training educates users about cybersecurity risks, best practices, and policies to reduce the likelihood of security incidents."]),
    (r"how to prevent ransomware attacks", ["To prevent ransomware attacks, you should regularly back up your data, keep your software up to date, avoid clicking on suspicious links or emails, use antivirus software, and restrict administrative privileges."]),
    (r"what is a denial of service attack", ["A Denial of Service (DoS) attack is a type of cyber attack where the attacker seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to the Internet."]),
    (r"how to secure my wifi network", ["To secure your Wi-Fi network, you should change the default name of your Wi-Fi network, enable WPA3 encryption, use a strong and unique password, turn off your Wi-Fi network when not in use, and consider using a guest network."]),
    (r"what is two factor authentication", ["Two-factor authentication (2FA) is a security process in which the user provides two different authentication factors to verify themselves. It is a type of multi-factor authentication."]),
    (r"what is a firewall", ["A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules."]),
    (r"how to protect my password", ["To protect your password, you should use a strong and unique password, avoid using the same password for multiple accounts, and consider using a password manager."]),
    (r"What is data encryption in transit",["Data encryption in transit protects information as it travels between systems or networks, ensuring confidentiality and integrity."]),
    (r"What is a security incident response plan",["A security incident response plan outlines procedures for detecting, responding to, and recovering from security incidents to minimize their impact."]),
    (r"what is encryption", ["Encryption is the process of converting plaintext data into unreadable ciphertext to protect it from unauthorized access."]),
]

# Initialize Chat with pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to handle user input and chatbot response
def send_message():
    user_input = message_entry.get()
    conversation_window.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot.respond(user_input)
    conversation_window.insert(tk.END, "ChatBot: " + response + "\n")
    message_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Mini Cyber Chatbot")
root.geometry("500x500")

# Create a scrolled text widget for the conversation
conversation_window = scrolledtext.ScrolledText(root, height=20, width=80)
conversation_window.pack(pady=20)

# Create an entry widget for the user to type their message
message_entry = tk.Entry(root, width=60)
message_entry.pack()

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
