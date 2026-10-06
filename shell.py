import psutil
import os
import shutil
import time


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage(path="/"):
    return psutil.disk_usage(path).percent


def get_top_process_by_cpu():
    processes = [
        (p.pid, p.info['name'], p.info['cpu_percent'])
        for p in psutil.process_iter(['name', 'cpu_percent'])
    ]

    processes.sort(key=lambda x: x[2], reverse=True)

    return processes[:3]


def clean_temp_files():
    temp_dir = '/tmp'

    if os.path.exists(temp_dir):
        try:
            shutil.rmtree(temp_dir)
            os.mkdir(temp_dir)

            print("[AI] Cleaned temporary files in /tmp")

        except Exception as e:
            print("[AI] Failed to clean /tmp:", e)

    else:
        print("[AI] No /tmp directory found")


# AI Logic / Expert Rules
def evaluate_system():

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    print("\n[System Stats]")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    print("\n[AI System Evaluation]")

    if cpu > 85:
        print("High CPU usage detected.")

        top_cpu = get_top_process_by_cpu()

        for pid, name, usage in top_cpu:
            print(
                f"Process {name} (PID {pid}) using {usage}% CPU"
            )

        # Optional: Automatically kill high CPU process
        # os.kill(pid, signal.SIGKILL)

    if memory > 80:
        print("High memory usage. Consider closing heavy apps.")

    if disk > 90:
        print("Low disk space. Running cleanup...")
        clean_temp_files()

    if cpu < 20 and memory < 30 and disk < 70:
        print("System is healthy. No action needed.")


# Run the program
if __name__ == "__main__":
    print("=== AI-Based System Monitor and Utility ===")
    evaluate_system()