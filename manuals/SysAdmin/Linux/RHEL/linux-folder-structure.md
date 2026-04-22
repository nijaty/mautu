# Структура Папок Linux

## Файловая система любого дистрибутива Linux содержит следующие каталоги:
- <span style="color: green;"><strong>/</strong></span> — корневой каталог;
- <span style="color: green;"><strong>/bin</strong></span> — содержит стандартные программы Linux (cat, ср, is, login и т. д.);
- <span style="color: green;"><strong>/boot</strong></span> — каталог загрузчика, содержит образы ядра и Initrd (RAM-диска инициализации), может содержать конфигурационные и вспомогательные файлы загрузчика;
- <span style="color: green;"><strong>/dev</strong></span> — содержит файлы устройств;
- <span style="color: green;"><strong>/etc</strong></span> — содержит конфигурационные файлы системы;
- <span style="color: green;"><strong>/home</strong></span> — содержит домашние каталоги пользователей;
- <span style="color: green;"><strong>/lib</strong></span> — библиотеки и модули;
- <span style="color: green;"><strong>/lost+found</strong></span> — восстановленные после некорректного размонтирования файловой системы файлы и каталоги;
- <span style="color: green;"><strong>/media</strong></span> — в некоторых дистрибутивах содержит точки монтирования сменных носителей (CD-, DVD-, USB-накопителей). Хотя файловые системы сменных дисков могут монтироваться и к другим каталогам;
- <span style="color: green;"><strong>/misc</strong></span> — может содержать все что угодно, равно как и каталог /opt;
- <span style="color: green;"><strong>/mnt</strong></span> — обычно содержит точки монтирования;
- <span style="color: green;"><strong>/opt</strong></span> — некоторые программы устанавливаются в этот каталог, хотя в последнее время такие программы встречаются все реже и реже;
- <span style="color: green;"><strong>/proc</strong></span> — каталог псевдофайловой системы procfs, предоставляющей информацию о процессах;
- <span style="color: green;"><strong>/root</strong></span> — каталог суперпользователя root;
- <span style="color: green;"><strong>/sbin</strong></span> — каталог системных утилит, выполнять которые имеет право пользователь root;
- <span style="color: green;"><strong>/tmp</strong></span> — каталог для временных файлов;
- <span style="color: green;"><strong>/usr</strong></span> — содержит пользовательские программы, документацию (папка /usr/share/doc), исходные коды программ и ядра (папка /usr/src);
- <span style="color: green;"><strong>/var</strong></span> — постоянно изменяющиеся данные системы — например, очереди системы печати, почтовые ящики, протоколы, замки и т.д.