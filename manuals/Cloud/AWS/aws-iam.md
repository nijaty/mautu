#  IAM (Управление Идентификацией и Доступом)

```
{
    "Version": "2012-10-17",
    "Id": "S3-Account-Permissions",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Principal": {
                "AWS": ["arn:aws:iam::123456789012:root"]
            },
            "Action": [
                "s3:Getobject"
                "s3:PutObject"
            ],
            "Resource": ["arn:aws:s3:::mybucket/*"]
        }
    ]
}

```
- <span style="color: green;"><strong>Version:</strong></span> версия языка политики, всегда указывайте "2012-10-17"
- <span style="color: green;"><strong>Id:</strong></span> идентификатор политики (необязательно)
- <span style="color: green;"><strong>Statement:</strong></span> одно или несколько отдельных утверждений (обязательно)
- <span style="color: green;"><strong>Sid:</strong></span> идентификатор утверждения (необязательно)
- <span style="color: green;"><strong>Effect:</strong></span> разрешает или запрещает ли утверждение доступ (Allow, Deny)
- <span style="color: green;"><strong>Principal:</strong></span> аккаунт/пользователь/роль, к которым применяется данная политика
- <span style="color: green;"><strong>Action:</strong></span> список действий, которые данная политика разрешает или запрещает
- <span style="color: green;"><strong>Resource:</strong></span> список ресурсов, к которым применяются действия
- <span style="color: green;"><strong>Condition:</strong></span> условия, при которых данная политика действует (необязательно)

