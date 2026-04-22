### ОСНОВЫ
<span style="color: green;"><strong>Cluster</strong></span>: Группа связанных компьютеров (узлов), которые запускают приложения.  
<span style="color: green;"><strong>Node</strong></span>: Отдельный компьютер в кластере, который запускает приложения.  
<span style="color: green;"><strong>Pod</strong></span>: Наименьшая единица в Kubernetes, которая может запускать один или несколько контейнеров.  

### НАГРУЗКИ (WORKLOADS)
<span style="color: green;"><strong>Deployment</strong></span>: Управляет набором одинаковых подов, обеспечивая нужное количество запущенных экземпляров.  
<span style="color: green;"><strong>ReplicaSet</strong></span>: Гарантирует, что заданное количество копий подов всегда запущено.  
<span style="color: green;"><strong>StatefulSet</strong></span>: Управляет stateful-приложениями, отслеживая идентичность каждого пода.  
<span style="color: green;"><strong>DaemonSet</strong></span>: Обеспечивает запуск пода на всех или выбранных узлах.  
<span style="color: green;"><strong>Job</strong></span>: Выполняет задачу до её успешного завершения.  
<span style="color: green;"><strong>CronJob</strong></span>: Запускает задачи по расписанию.  

### СЕТЬ (NETWORKING)
<span style="color: green;"><strong>Service</strong></span>: Предоставляет доступ к набору подов как к сетевому сервису.  
<span style="color: green;"><strong>ClusterIP Service</strong></span>: Открывает сервис внутри кластера.  
<span style="color: green;"><strong>NodePort Service</strong></span>: Открывает сервис через статический порт на каждом узле.  
<span style="color: green;"><strong>LoadBalancer Service</strong></span>: Открывает сервис снаружи через балансировщик нагрузки облачного провайдера.  
<span style="color: green;"><strong>Headless Service</strong></span>: Сервис без Cluster IP, используется для прямого доступа к подам.  
<span style="color: green;"><strong>Ingress</strong></span>: Управляет внешним доступом к сервисам (обычно HTTP).  
<span style="color: green;"><strong>Ingress Controller</strong></span>: Обрабатывает маршрутизацию Ingress (HTTP/HTTPS).  
<span style="color: green;"><strong>Endpoints</strong></span>: Список IP-адресов и портов, на которые сервис направляет трафик.  
<span style="color: green;"><strong>NetworkPolicy</strong></span>: Управляет сетевым трафиком между подами.  

### ХРАНИЛИЩЕ (STORAGE)
<span style="color: green;"><strong>Volume</strong></span>: Предоставляет хранилище для контейнеров.  
<span style="color: green;"><strong>PersistentVolume (PV)</strong></span>: Выделенное хранилище в кластере.  
<span style="color: green;"><strong>PersistentVolumeClaim (PVC)</strong></span>: Запрос пользователя на хранилище.  
<span style="color: green;"><strong>StorageClass</strong></span>: Определяет типы доступного хранилища.  
<span style="color: green;"><strong>EmptyDir</strong></span>: Временное хранилище, существующее пока живёт под.  

### КОНФИГУРАЦИЯ И СЕКРЕТЫ
<span style="color: green;"><strong>ConfigMap</strong></span>: Хранит конфигурационные данные в виде пар ключ-значение.  
<span style="color: green;"><strong>Secret</strong></span>: Хранит чувствительные данные (пароли, токены).  

### ПЛАНИРОВАНИЕ И РАЗМЕЩЕНИЕ
<span style="color: green;"><strong>Scheduler</strong></span>: Назначает поды на узлы.  
<span style="color: green;"><strong>Taints</strong></span>: Запрещают запуск определённых подов на узлах.  
<span style="color: green;"><strong>Tolerations</strong></span>: Позволяют подам запускаться на узлах с taints.  
<span style="color: green;"><strong>Affinity/Anti-Affinity</strong></span>: Правила размещения подов.  
<span style="color: green;"><strong>Priority Class</strong></span>: Определяет приоритет подов при планировании.  

### БЕЗОПАСНОСТЬ
<span style="color: green;"><strong>Role-Based Access Control (RBAC)</strong></span>: Управляет правами доступа.  
<span style="color: green;"><strong>Role</strong></span>: Права доступа внутри namespace.  
<span style="color: green;"><strong>ClusterRole</strong></span>: Права доступа на уровне всего кластера.  
<span style="color: green;"><strong>RoleBinding</strong></span>: Назначает Role пользователям/группам.  
<span style="color: green;"><strong>ClusterRoleBinding</strong></span>: Назначает ClusterRole глобально.  
<span style="color: green;"><strong>ServiceAccount</strong></span>: Идентификатор для подов.  
<span style="color: green;"><strong>Security Context</strong></span>: Определяет параметры безопасности пода/контейнера.  
<span style="color: green;"><strong>PodSecurityPolicy</strong></span>: Определяет правила безопасности для подов.  

### КОМПОНЕНТЫ КЛАСТЕРА
<span style="color: green;"><strong>Kubelet</strong></span>: Работает на узлах и управляет подами.  
<span style="color: green;"><strong>Kube-Proxy</strong></span>: Управляет сетевыми правилами.  
<span style="color: green;"><strong>Controller Manager</strong></span>: Запускает контроллеры.  
<span style="color: green;"><strong>Etcd</strong></span>: Хранит состояние кластера.  
<span style="color: green;"><strong>CoreDNS</strong></span>: Обеспечивает DNS внутри кластера.  

### МАСШТАБИРОВАНИЕ
<span style="color: green;"><strong>Horizontal Pod Autoscaler (HPA)</strong></span>: Масштабирует поды по нагрузке.  
<span style="color: green;"><strong>Vertical Pod Autoscaler (VPA)</strong></span>: Настраивает ресурсы подов.  
<span style="color: green;"><strong>Cluster Autoscaler</strong></span>: Изменяет количество узлов.  

### ЖИЗНЕННЫЙ ЦИКЛ ПОДА
<span style="color: green;"><strong>Init Containers</strong></span>: Запускаются перед основными контейнерами.  
<span style="color: green;"><strong>Sidecar Container</strong></span>: Вспомогательный контейнер в поде.  
<span style="color: green;"><strong>Readiness Probe</strong></span>: Проверяет готовность контейнера.  
<span style="color: green;"><strong>Liveness Probe</strong></span>: Проверяет состояние контейнера.  
<span style="color: green;"><strong>PodDisruptionBudget (PDB)</strong></span>: Ограничивает количество недоступных подов.  

### УПРАВЛЕНИЕ РЕСУРСАМИ
<span style="color: green;"><strong>Resource Requests</strong></span>: Минимально необходимые ресурсы.  
<span style="color: green;"><strong>Resource Limits</strong></span>: Максимально допустимые ресурсы.  
<span style="color: green;"><strong>Resource Quotas</strong></span>: Ограничивает ресурсы namespace.  
<span style="color: green;"><strong>LimitRange</strong></span>: Ограничения ресурсов для контейнеров.  

### МЕТАДАННЫЕ
<span style="color: green;"><strong>Label</strong></span>: Пары ключ-значение для выбора объектов.  
<span style="color: green;"><strong>Annotation</strong></span>: Дополнительные метаданные.  

### ПРОСТРАНСТВА ИМЁН (NAMESPACE)
<span style="color: green;"><strong>Namespace</strong></span>: Логическое разделение ресурсов.  
<span style="color: green;"><strong>Default Namespace</strong></span>: Namespace по умолчанию.  

### ИНСТРУМЕНТЫ
<span style="color: green;"><strong>Kubectl</strong></span>: CLI для работы с Kubernetes.  
<span style="color: green;"><strong>Helm</strong></span>: Пакетный менеджер Kubernetes.  
<span style="color: green;"><strong>Helm Chart</strong></span>: Пакет ресурсов Kubernetes.  
<span style="color: green;"><strong>Kustomize</strong></span>: Инструмент кастомизации YAML.  

### ПРОДВИНУТОЕ
<span style="color: green;"><strong>Custom Resource Definition (CRD)</strong></span>: Расширяет API Kubernetes.  
<span style="color: green;"><strong>Operator</strong></span>: Автоматизирует управление сложными приложениями.  
<span style="color: green;"><strong>Admission Controller</strong></span>: Проверяет/изменяет API-запросы.  
<span style="color: green;"><strong>Finalizer</strong></span>: Обеспечивает очистку перед удалением.  

### РАЗВЁРТЫВАНИЕ КЛАСТЕРА
<span style="color: green;"><strong>Kubeadm</strong></span>: Инструмент для развертывания кластера.  
<span style="color: green;"><strong>Minikube</strong></span>: Локальный одновузловой Kubernetes.  

### АРХИТЕКТУРА
<span style="color: green;"><strong>Master Node</strong></span>: Управляет кластером.  
<span style="color: green;"><strong>Worker Node</strong></span>: Запускает приложения и поды.  

### КОНЦЕПЦИИ
<span style="color: green;"><strong>Self-healing</strong></span>: Автоматически восстанавливает упавшие контейнеры.  
<span style="color: green;"><strong>Secrets Management</strong></span>: Управляет чувствительными данными.  

### Источник:

- DevopsDiaries
