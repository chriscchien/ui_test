class SettingPage():
    def __init__(self):        

        # Locators
        self.allow_collecting_longhorn_usage_metrics = '//form/div[1]/div/div[1]/div/div/span/span'
        self.allow_collecting_longhorn_usage_metrics_enable = "#allow-collecting-longhorn-usage-metrics"
        self.allow_collecting_longhorn_usage_metrics_require_icon = "//form/div[1]/div/div[1]/div/div/span/div/i"        
        self.allow_collecting_longhorn_usage_detail_description = "//form/div[1]/div/div[1]/div/div/span/div/small"

        self.automatically_delete_workload_pod_when_the_volume_is_detached_unexpectedly = "//form/div[1]/div/div[2]/div/div/span/span"
        self.automatically_delete_workload_pod_when_the_volume_is_detached_unexpectedly_enable = ""
        self.automatically_delete_workload_pod_when_the_volume_is_detached_unexpectedly_require = ""
        self.automatically_delete_workload_pod_when_the_volume_is_detached_unexpectedly_detail_description = ""
