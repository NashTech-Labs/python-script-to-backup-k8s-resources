import subprocess


def backup_kubernetes_resources(output_directory, kubeconfig_path):
    backup_file = f"kubernetes_backup.yaml"

    try:
        subprocess.run(["kubectl", "--kubeconfig", kubeconfig_path, "get", "all", "--all-namespaces", "-o", "yaml"], capture_output=True, text=True, check=True)
        output = subprocess.check_output(["kubectl", "--kubeconfig", kubeconfig_path, "get", "all", "--all-namespaces", "-o", "yaml"], text=True)
        
        with open(f"{output_directory}/{backup_file}", "w") as file:
            file.write(output)
        
        print(f"Backup completed successfully. Saved to {output_directory}/{backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")
    
if __name__ == "__main__":
    backup_kubernetes_resources("path_to_your_backup_directory", "path_to_your_kube_config_file")
