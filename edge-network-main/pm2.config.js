module.exports = {
    apps: [
        {
            name: 'mqtt_broker',
            script: 'mqtt_broker.py',
            interpreter: 'python3',
            watch: true,
            ignore_watch: ['node_modules', 'logs', 'errors'], // Add any folders you want to ignore during watch
            autorestart: true,
            log_date_format: 'YYYY-MM-DD HH:mm:ss Z', // Log timestamp format
            out_file: './logs/mqtt_broker.log',        // Path to the log file
            error_file: './errors/mqtt_broker_error.log', // Path to the error log file
            merge_logs: true,                         // Merge logs from different instances
        },
        {
            name: 'bluetooth_scanner',
            script: 'bluetooth_scanner.py',
            interpreter: 'python3', // Use 'python' for Python 2
            watch: true,
            ignore_watch: ['node_modules', 'logs', 'errors'], // Add any folders you want to ignore during watch
            autorestart: true,
            log_date_format: 'YYYY-MM-DD HH:mm:ss Z', // Log timestamp format
            out_file: './logs/bluetooth_scanner.log',        // Path to the log file
            error_file: './errors/bluetooth_scanner_error.log', // Path to the error log file
            merge_logs: true,                         // Merge logs from different instances
        },
        {
            name: 'wifi_scanner',
            script: 'wifi_scanner.py',
            interpreter: 'python3', // Use 'python' for Python 2
            watch: true,
            ignore_watch: ['node_modules', 'logs', 'errors'], // Add any folders you want to ignore during watch
            autorestart: true,
            log_date_format: 'YYYY-MM-DD HH:mm:ss Z', // Log timestamp format
            out_file: './logs/wifi_scanner.log',        // Path to the log file
            error_file: './errors/wifi_scanner_error.log', // Path to the error log file
            merge_logs: true,                         // Merge logs from different instances
        },
        {
            name: 'Hermes',
            script: 'hermes.py',
            interpreter: 'python3', // Use 'python' for Python 2
            watch: true,
            ignore_watch: ['node_modules', 'logs', 'errors'], // Add any folders you want to ignore during watch
            autorestart: true,
            log_date_format: 'YYYY-MM-DD HH:mm:ss Z', // Log timestamp format
            out_file: './logs/hermes.log',        // Path to the log file
            error_file: './errors/hermes.log', // Path to the error log file
            merge_logs: true,                         // Merge logs from different instances
        },
    ],
};
