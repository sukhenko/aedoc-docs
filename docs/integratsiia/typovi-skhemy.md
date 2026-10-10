# Типові схеми руху підакцизних товарів

## Типове рішення інтеграції підсистеми АЕДос для роздрібної мережі

Автоматизація обліку обігу акцизних марок: облікова система з інтегрованою підсистемою AEDOC, каса ПРРО, ТСД на прийманні та обмін з еАкциз через API Excise.

### Можливості підсистеми

<div class="cards cards--features" markdown>

<a class="card" href="../skhovyshche-marok/">
<strong>Сховище марок</strong>
<span>HTTP-сервіс для ПРРО: визначає статус акцизної марки при продажу та поверненні. Синхронізований з обліковою базою.</span>
<span class="card__more">Детальніше →</span>
</a>

<a class="card" href="../zberigannia/zovnishnie-skhovyshche/">
<strong>Зовнішнє сховище MSSQL</strong>
<span>Дані обміну та документи еАкциз зберігаються в окремій базі MSSQL — без навантаження на основну облікову базу.</span>
<span class="card__more">Детальніше →</span>
</a>

<a class="card" href="../../navchannia/">
<strong>Курс навчання</strong>
<span>Навчальний курс для роботи з підсистемою: від налаштування до щоденних операцій касира та комірника.</span>
<span class="card__more">Перейти до курсу →</span>
</a>

</div>

## Схема роботи підсистеми AEDOC для роздрібної мережі

<img class="schema" src="../img/skhema-rozdrib.svg" alt="Схема: облікова система з AEDOC, каса ПРРО, ТСД, еАкциз і ЦОД РРО та зв'язки між ними">

### Основні переваги

<div class="wf wf--4">

<div class="wf__step">
<strong>Контроль статусів акцизних марок</strong>
<span>Перевірка статусу марки при продажу або переміщенні. Запобігає повторному списанню.</span>
</div>

<div class="wf__step">
<strong>Відповідність приходу та марок</strong>
<span>Контроль відповідності надходження продукції та акцизних марок за кожним документом.</span>
</div>

<div class="wf__step">
<strong>Проста робота з протоколами сканування</strong>
<span>Завантаження протоколів із ТСД в облікову систему без ручного введення.</span>
</div>

<div class="wf__step">
<strong>Автоматизоване повернення</strong>
<span>Повернення марок в обіг через чеки повернення ПРРО.</span>
</div>

</div>

<div class="callout callout--gold" markdown>

### Тестування без ризику

Перевірте інтеграцію на тестовому контурі еАкциз — бойові дані не зачіпаються.

<div class="wf">

<div class="wf__step">
<strong>Реєстрація в тестовому еАкциз</strong>
<a class="wf__link" href="../../pershyi-zapusk/reiestratsiia-eo/">xtrace.gov.ua →</a>
</div>

<div class="wf__step">
<strong>API-токен</strong>
<a class="wf__link" href="../../pershyi-zapusk/api-token/">Інструкція →</a>
</div>

<div class="wf__step">
<strong>Встановлення тестової конфігурації</strong>
<a class="wf__link" href="../sandbox/">Завантажити .msi →</a>
</div>

<div class="wf__step">
<strong>Майстер нового ЕО</strong>
<a class="wf__link" href="../../pershyi-zapusk/pomichnyk-eo/">Інструкція →</a>
</div>

<div class="wf__step">
<strong>Тестові АЕД</strong>
<a class="wf__link" href="https://t.me/AEDocBot">Запит у підтримку →</a>
</div>

</div>

У пакеті: AEDocSignService (КЕП), розширення для конфігурацій на керованих формах, конфігурація для інтеграції на звичайних формах — з налаштованим тестовим сервером.

[Отримати тестовий пакет](https://t.me/AEDocBot){ .md-button .md-button--primary }

</div>

## Типові сценарії обліку в роздрібній мережі

Повний цикл руху підакцизного товару з інтегрованим еАкциз

<div class="flow-nav">
<a href="#flow-1"><span>1</span>Отримання і продаж в роздріб</a>
<a href="#flow-2"><span>2</span>Відмова від АЕД</a>
<a href="#flow-3"><span>3</span>ПпН · Коригування АЕД</a>
<a href="#flow-4"><span>4</span>Повернення постачальнику</a>
</div>

<p class="flow-label">Сценарій 1 з 4</p>

### Отримання і продаж в роздріб {#flow-1}

Повний цикл руху підакцизного товару від постачальника до кінцевого споживача

<div class="flow">

<div class="flow__step flow--aed">
<span class="flow__tag">АЕД №1</span>
<strong class="flow__title">Отримання від постачальника</strong>
<ul>
<li>Прийом документа з еАкциз (вхідний)</li>
<li>Протокол сканування марок при прийомі</li>
<li>Підпис КЕП одержувачем</li>
<li>Синхронізація статусу з xtrace.gov.ua</li>
</ul>
</div>

<div class="flow__step flow--invoice">
<span class="flow__tag">Прибуткова</span>
<strong class="flow__title">Прибуткова накладна</strong>
<ul>
<li>Створюється на підставі АЕД №1</li>
<li>Товар прибуткується на центральний склад</li>
</ul>
</div>

<div class="flow__step flow--transfer">
<span class="flow__tag">Переміщення</span>
<strong class="flow__title">Переміщення на торгову точку</strong>
<ul>
<li>Внутрішній документ переміщення</li>
<li>Товар готується для роздрібної мережі</li>
</ul>
</div>

<div class="flow__step flow--aed">
<span class="flow__tag">АЕД №7</span>
<strong class="flow__title">Внутрішнє переміщення в еАкциз</strong>
<ul>
<li>Створюється на підставі переміщення</li>
<li>Підпис КЕП відправника (центральний склад)</li>
<li>Підпис КЕП одержувача (торгова точка)</li>
<li>Обидва підписи — обов'язкові</li>
<li>Товар у роздрібній мережі</li>
</ul>
</div>

<div class="flow__step flow--prro">
<span class="flow__tag">Чек ПРРО</span>
<strong class="flow__title">Продаж кінцевому споживачеві</strong>
<ul>
<li>Контроль наявності марки на торговій точці</li>
<li>Контроль що марка НЕ погашена</li>
<li>Погашення марки при пробитті чека</li>
</ul>
</div>

<div class="flow__step flow--return">
<span class="flow__tag">Чек ПРРО повернення</span>
<strong class="flow__title">Повернення від покупця (в роздріб)</strong>
<ul>
<li>Пробиття чека повернення в ПРРО</li>
<li>Марка автоматично "розпогашається", товар — на торгову точку</li>
</ul>
</div>

</div>

<p class="flow-label">Сценарій 2 з 4</p>

### Відмова від АЕД {#flow-2}

Отримувач відмовляється приймати товар — АЕД анулюється

<div class="flow">

<div class="flow__step flow--aed">
<span class="flow__tag">АЕД №1</span>
<strong class="flow__title">Постачальник надіслав АЕД</strong>
<ul>
<li>Документ надходить у чергу AEDOC</li>
<li>Статус: Отримано, очікує реакції отримувача</li>
</ul>
</div>

<div class="flow__step flow--return">
<span class="flow__tag">Дія отримувача</span>
<strong class="flow__title">Відмова від отримання</strong>
<ul>
<li>Відкрийте АЕД який не хочете приймати на баланс</li>
<li>Натисніть кнопку "Відмовитись від АЕД"</li>
<li>Вкажіть причину відмови</li>
</ul>
</div>

<div class="flow__step flow--aed">
<span class="flow__tag">АЕД №1</span>
<strong class="flow__title">Очікування підпису постачальника</strong>
<ul>
<li>АЕД повертається постачальнику з ознакою відмови</li>
<li>Постачальник має підписати відмову власним КЕП</li>
<li>Статус у AEDOC: Очікує підтвердження відмови</li>
</ul>
</div>

<div class="flow__step flow--canceled">
<span class="flow__tag">Анульовано</span>
<strong class="flow__title">АЕД остаточно анульовано в еАкциз</strong>
<ul>
<li>Після підпису постачальника — статус змінюється на Анульовано</li>
<li>Товар НЕ прибуткується у BAS. Марки не змінюють свій статус.</li>
</ul>
</div>

</div>

<p class="flow-label">Сценарій 3 з 4</p>

### ПпН · Коригування АЕД {#flow-3}

Виявлено розбіжності в АЕД — фіксуємо і узгоджуємо з постачальником

<div class="flow">

<div class="flow__step flow--aed">
<span class="flow__tag">АЕД №1</span>
<strong class="flow__title">Отримано АЕД з розбіжностями</strong>
<ul>
<li>При скануванні марок виявлено невідповідність</li>
<li>Розбіжності зафіксовані в протоколі сканування</li>
<li>На формі АЕД доступна кнопка "Створити ПпН"</li>
</ul>
</div>

<div class="flow__step flow--ppn">
<span class="flow__tag">ПпН</span>
<strong class="flow__title">Створення Протоколу про невідповідність</strong>
<ul>
<li>Створюється на підставі отриманого АЕД</li>
<li>Автозаповнення розбіжностей з протоколу сканування:</li>
<li>надлишок або недостача по кількості акцизних марок</li>
</ul>
</div>

<div class="flow__step flow--ppn">
<span class="flow__tag">ПпН</span>
<strong class="flow__title">Підпис і відправка постачальнику</strong>
<ul>
<li>Підпис КЕП відправника (наша сторона)</li>
<li>ПпН надсилається постачальнику через еАкциз</li>
</ul>
</div>

<div class="flow__step flow--aed">
<span class="flow__tag">Реакція постачальника</span>
<strong class="flow__title">Один з трьох сценаріїв</strong>
<ul>
<li>А. Постачальник виправляє АЕД → надсилає новий</li>
<li>Б. Постачальник підписує ПпН (погоджується з розбіжностями)</li>
<li>В. Постачальник відхиляє ПпН → потрібне узгодження</li>
<li>АЕД і ПпН залишаються пов'язаними в системі</li>
</ul>
</div>

<div class="flow__step flow--invoice">
<span class="flow__tag">Прибуткова</span>
<strong class="flow__title">Прибуткова накладна після узгодження</strong>
<ul>
<li>Після виправлення АЕД товар приймається на баланс</li>
<li>Кількість у BAS відповідає фактично прийнятому</li>
</ul>
</div>

</div>

<p class="flow-label">Сценарій 4 з 4</p>

### Повернення постачальнику {#flow-4}

АЕД №4 або №5 створюється на підставі раніше прийнятого АЕД №1

<div class="flow">

<div class="flow__step flow--aed">
<span class="flow__tag">АЕД №1</span>
<strong class="flow__title">Раніше прийнятий АЕД (підстава)</strong>
<ul>
<li>АЕД №1 від постачальника, що вже підписаний і прийнятий</li>
<li>Товар на балансі. Виникла потреба повернути постачальнику.</li>
</ul>
</div>

<div class="flow__step flow--return">
<span class="flow__tag">АЕД №4 / №5</span>
<strong class="flow__title">Створення на підставі АЕД №1</strong>
<ul>
<li>На формі АЕД №1 доступна дія "Створити АЕД повернення"</li>
<li>АЕД №4 — звичайне повернення покупцем</li>
<li>АЕД №5 — повернення для усунення виявлених недоліків</li>
<li>Перелік марок автоматично переноситься з АЕД №1</li>
<li>Кількість можна редагувати (часткове повернення)</li>
</ul>
</div>

<div class="flow__step flow--return">
<span class="flow__tag">АЕД №4 / №5</span>
<strong class="flow__title">Підпис і відправка постачальнику</strong>
<ul>
<li>Підпис КЕП відправника (наша сторона)</li>
<li>АЕД надсилається постачальнику через еАкциз</li>
<li>Очікування підпису отримувача (постачальника)</li>
</ul>
</div>

<div class="flow__step flow--invoice">
<span class="flow__tag">Видаткова</span>
<strong class="flow__title">Видаткова накладна (повернення)</strong>
<ul>
<li>Створюється на підставі АЕД №4 / №5</li>
<li>Товар списується з залишків BAS</li>
<li>Марки знімаються з обліку у нас</li>
</ul>
</div>

</div>
