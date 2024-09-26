# Анализ логов полётного контроллера PX4

Бывает такое что необходимо проанализировать показания с датчиков и это могут сделать лишь те кто в этом разбираються. И для того чтоб проанализировать эти логи мы предлогаем неиронную сеть которая возврощает список событий происходящих с дроном во времени. 

![Неиронка](https://github.com/StasFoster/Havaton_BRICKS2024/blob/129f427b5b63c12abe42bd3dd447109fffaca6cc/%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0/1643325841_73-kartinkin-net-p-pattern-neiroset-krasivie-79.jpg)

## Реалезация
### Первоначальное преоброзование

Перед тем как неиронка будет анализировать логи мы преобразуем их при помощи сервиса https://logs.px4.io (из .ulg в .params)

### Структура неиронной сети необходимой для оброботки

При создании неронки мы использовали язык программирования Python в частности библиотеки Tensorflow и Keras. Библиотеки содержат различные виды слоёв для реализации различных структур неиронных сетей (Denese, Conv2D и т.п.). Нам для ревлезации данной задачи необходимо использовать рекуретные слои которые лучше подходят для обработки последовательности информации нежели теже полносвязные слои.

### Датасет







![Изображение](https://github.com/StasFoster/Havaton_BRICKS2024/blob/9e2722fc1f288f2e9701958fecf5a823fcf5d247/%D0%AD%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF%20%D0%9E%D0%B4%D0%BD%D0%B8%D0%BC%20%D0%A6%D0%B5%D0%BB%D1%8B%D0%BC.png)

## Название команды / The name of the team

Команда / Team - Одним Целым

## Описание команды / Team description

Наша дружная команда собралась для выполнения достаточно важной цели, обеспечить Беспилотные Летающие Аппараты (БПЛА) системой самодиагностики. Можно в точности сказать, что какой бы трудной ни была данная задача, наша команда обязательно справится со всеми препятствиями на дорогое к достижению цели. / Our friendly team has gathered to fulfill a rather important goal, to provide Unmanned Aerial Vehicles (UAVs) with a self-diagnosis system. We can say for sure that no matter how difficult this task may be, our team will definitely cope with all the obstacles on the way to achieving the goal.

## Состав команды / The team consist

* **Шустов Станислав** / **Shustov Stanislav** (Капитан команды / Team leader).

* **Сергеев Станислав** / **Sergeev Stanislav** (Дата Специалист / Data Specialist). 

* **Бисаров Алексей** / **Bisarov Aleksey** (ИИ Специалист / AI Specialist).

## Описание участников / Description of the participants

* **Шустов Станислав** - наш капитан команды. Его навыкам в сборке и программировании дронов можно только позавидовать. Он собрал нас вместе для участия в этом замечательном конкурсе, чтобы мы могли получить ценный опыт работы в команде. / Shustov Stanislav is our team captain. His skills in assembling and programming drones can only be envied. He brought us together to participate in this wonderful competition so that we could gain valuable team experience.

* **Станислав Сергеев** - специалист в машинном обучении нейронных сетей. В команде отвечает за подбор правильных данных для обучения нейросети, а также за правильную их интеграцию в код нейросети. / Sergeev Stanislav is a specialist in machine learning of neural networks. In the team, he is responsible for selecting the correct data for neural network training, as well as for their correct integration into the neural network code.

* **Бисаров Алексей** - специалист в сфере создания нейронных сетей. Он разбирается во всех тонкостях нейросетей, и может адаптировать их под разные задачи. / Bisarov Aleksey is a specialist in the field of creating neural networks. He understands all the intricacies of neural networks, and can adapt them to different tasks.

## Конкурсное задание / The competitive task

Самодиагностика БПЛА, с применением нейронной сети для обнаружения и диагностики повреждений во время полета. / Self-diagnosis of UAVs, using a neural network to detect and diagnose damage during flight.


[TaskBoard](https://docs.google.com/spreadsheets/d/1PIl7bhBPtqOBv_UBM3XKtVbSxh-o-9a6cCnWLpuicuM/edit?usp=sharing)



















