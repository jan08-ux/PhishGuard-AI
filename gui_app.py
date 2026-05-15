import tkinter as tk
from tkinter import ttk, messagebox
from detector import PhishingDetector  # Direct import

class PhishingDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing URL Detector")
        self.setup_ui()
        try:
            self.detector = PhishingDetector()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {str(e)}")
            self.root.destroy()
    
    def setup_ui(self):
        ttk.Label(self.root, text="Enter URL:").pack(pady=10)
        self.url_entry = ttk.Entry(self.root, width=50)
        self.url_entry.pack()
        
        ttk.Button(self.root, text="Check URL", command=self.check_url).pack(pady=10)
        
        self.result_frame = ttk.LabelFrame(self.root, text="Results")
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.result_text = tk.Text(self.result_frame, height=10, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        ttk.Button(self.root, text="Clear", command=self.clear).pack(pady=5)
    
    def check_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Please enter a URL")
            return
        
        try:
            result = self.detector.predict(url)
            self.show_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def show_result(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"URL: {result['url']}\n\n")
        self.result_text.insert(tk.END, f"Status: {'PHISHING' if result['is_phishing'] else 'SAFE'}\n")
        self.result_text.insert(tk.END, f"Confidence: {result['confidence']:.2%}\n\n")
        self.result_text.insert(tk.END, "Analysis:\n")
        
        for reason in result['reasons']:
            self.result_text.insert(tk.END, f"- {reason}\n")
        
        # Color coding
        tag = 'phishing' if result['is_phishing'] else 'safe'
        self.result_text.tag_add(tag, '1.0', tk.END)
        self.result_text.tag_config('phishing', foreground='red')
        self.result_text.tag_config('safe', foreground='green')
    
    def clear(self):
        self.url_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingDetectorApp(root)
    root.mainloop()