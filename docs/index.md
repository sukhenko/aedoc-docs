---
hide:
  - toc
---

# Довідка AEDOC { .visually-hidden }

<div class="hero" markdown>

<p class="hero__eyebrow">AEDOC — інтеграція еАкциз з обліковими системами і ПРРО / РРО</p>

<p class="hero__title">Акцизні документи, підпис і марки — в одній базі, без входу в кабінет еАкциз</p>

<p class="hero__lead">Тут зібрано все для впровадження і щоденної роботи: технічні вимоги, інструкції з реальних тестів, відео та довідники.</p>

<div class="dl dl--hero">
<a class="dl__btn dl__btn--gold" href="https://aedoc.com.ua/download/%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%8f-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d1%86%d1%96%d1%97-%d0%b0%d0%b5%d0%b4%d0%be%d1%81-%d0%b5%d0%b0%d0%ba/?wpdmdl=1100&amp;masterkey=O9dcV8_ycmVqIXQktj0R3wCUZCvq4lylBo8OMxiQx9OZ8MXji0Jw51zc-ZujyD3AiFu3OYeX-0RPAWOekI4xLl3nt6g2-02p7RyS-Dg4yaAQ"><span class="dl__ico">⬇</span><span><b>Конфігурація</b><small>CF · 1,5 МБ · v1.0.1.7 від 01.10.2026</small></span></a>
<a class="dl__btn" href="https://aedoc.com.ua/download/%d1%80%d0%be%d0%b7%d1%88%d0%b8%d1%80%d0%b5%d0%bd%d0%bd%d1%8f-%d0%b0%d0%b5%d0%b4%d0%be%d0%ba-%d0%b4%d0%bb%d1%8f-%d1%96%d0%bd%d1%82%d0%b5%d0%b3%d1%80%d0%b0%d1%86%d1%96%d1%97-bas-%d0%bc%d0%b0%d0%bb%d0%b8/?wpdmdl=961&amp;masterkey=OcfrThd5vLXuNNHUTBwEwV78gnSI2OGMMOViLd_7AeNiCmjAjv9N9ojm0AmCJY_pDjQA0hE6DZtF46YpioVLUur6G0LQWgZCSQjkqyYMdOmA"><span class="dl__ico">⬇</span><span><b>Розширення «Малий бізнес»</b><small>v1.0.1.7 від 01.10.2026 · керовані форми</small></span></a>
<a class="dl__btn" href="https://aedoc.com.ua/download/%d0%bc%d0%be%d0%b4%d1%83%d0%bb%d1%8c-%d0%bf%d1%96%d0%b4%d0%bf%d0%b8%d1%81%d1%83-%d0%b5%d0%b0%d0%ba%d1%86%d0%b8%d0%b7/"><span class="dl__ico">🔐</span><span><b>Служба підпису AEDocSignService</b><small>обов'язкова для обох поставок</small></span></a>
</div>

<ol class="hero__steps">
<li><a href="integratsiia/"><strong>Інтегруйте / встановіть підсистему AEDOC</strong></a> — передайте інформацію з інтеграції спеціалісту з вашої облікової системи (програмісту).</li>
<li><a href="pershyi-zapusk/"><strong>Перший запуск і додавання ЕО</strong></a> — реєстрація в еАкциз, API-токен, <a href="pershyi-zapusk/pomichnyk-eo/">помічник додавання ЕО</a>.</li>
<li><strong>Пройдіть навчання</strong> роботи з типовими механізмами <a href="dovidnyky/korystuvachi-eo-kliuch/">підпису</a> і АЕД:
<span class="hero__links">
<a href="aed/pryiom-vkhidnoho-aed/">Прийняти вхідний АЕД</a>
<a href="aed/vidkhylennia-aed1/">Відмовитися від АЕД</a>
<a href="aed/aed4-povernennia/">Повернути АЕД</a>
<a href="dovidnyky/dostup-do-obiektiv/">Надати контрагенту доступ до ваших об'єктів для обміну АЕД</a>
</span></li>
</ol>

</div>

## Як це працює: від АЕД до чека

<div class="home-video" markdown>

<div class="video"><iframe src="https://www.youtube.com/embed/lT_LjHRXzEg" title="Тестування еАкциз: Інтеграція з Роздріб ред.1 (звичайні форми) та ПРРО" allowfullscreen></iframe></div>

<div class="home-video__text" markdown>

**5 хвилин — повний цикл акцизних марок в одній базі.**

Тестове відео на конфігурації Роздріб ред.1 з інтегрованим ПРРО ВебЧек:

1. **Прийом марок** — вхідний АЕД від постачальника, протокол сканування марок.
2. **Підпис** — АЕД підписано отримувачем, квитанції 1 і 2 з еАкциз.
3. **Продаж через ПРРО ВебЧек** — каса перевіряє марку: погашена в чек не потрапить, прийнята — продається і йде в еАкциз на погашення.

Без ручного введення і без входу в кабінет еАкциз.

[Детальніше про тест →](testuvannia/rozdrib-prro.md)

</div>

</div>

## Чому AEDOC

<div class="cards cards--features" markdown>

<div class="card">
<strong>Усе в обліковій базі</strong>
<span>Прийом, підпис, відхилення і повернення АЕД виконуються прямо в обліковій системі BAS. Кабінет еАкциз відкривати не потрібно.</span>
</div>

<div class="card">
<strong>Підпис КЕП з облікової системи</strong>
<span>Служба підпису AEDocSignService підписує документи ключем користувача: обрали підписанта — ключ і пароль підставились.</span>
</div>

<div class="card">
<strong>Перевірка марок без ручного введення</strong>
<span>Протокол сканування: сканер штрихкоду, ТСД або масова відмітка. Розбіжності йдуть в еАкциз автоматично.</span>
</div>

<div class="card">
<strong>Продаж через ПРРО з контролем марки</strong>
<span>Під час продажу каса перевіряє марку: погашена в чек не потрапить, прийнята — йде в еАкциз на погашення.</span>
</div>

<div class="card">
<strong>Під вашу конфігурацію</strong>
<span>Керовані і звичайні форми, розширення або окрема (standalone) конфігурація — зручно і для роботи, і для тестування.</span>
</div>

<div class="card">
<strong>Перевірено навантаженням</strong>
<span>Тест на 1000 АЕД і 1 млн марок: відомо, як росте база і що можна винести в зовнішнє сховище MS SQL.</span>
</div>

</div>

## Хто ви? { #start }

Оберіть свою роль — покажемо, з чого почати.

=== "Налаштовую систему"

    <p class="role-lead">Адміністратор або впроваджувач: підключаєте організацію до еАкциз і готуєте AEDOC до роботи.</p>

    1. [Зареєструйтесь економічним оператором в еАкциз](pershyi-zapusk/reiestratsiia-eo.md)
    2. [Отримайте API-токен](pershyi-zapusk/api-token.md)
    3. [Додайте організацію помічником ЕО](pershyi-zapusk/pomichnyk-eo.md)
    4. [Налаштуйте підпис і доступи](pershyi-zapusk/nastupni-kroky.md)
    5. [Оновіть користувачів ЕО і встановіть ключ ЕЦП](dovidnyky/korystuvachi-eo-kliuch.md)
    6. [Надайте контрагентам доступ до ваших торгових об'єктів](dovidnyky/dostup-do-obiektiv.md)
    7. Перевірте все першим документом — [прийміть вхідний АЕД №1](aed/pryiom-vkhidnoho-aed.md)

=== "Хочу навчитися"

    <p class="role-lead">Користувач (бухгалтер, комірник, оператор): щодня працюєте з акцизними документами.</p>

    1. Подивіться [відео повного циклу](testuvannia/rozdrib-prro.md) — 5 хвилин, щоб побачити картину цілком
    2. Прочитайте [рекомендований порядок навчання](navchannia/index.md)
    3. [Прийміть вхідний АЕД №1](aed/pryiom-vkhidnoho-aed.md): протокол сканування, підпис, обмін
    4. [Відхиліть вхідний АЕД №1](aed/vidkhylennia-aed1.md), якщо марки не відповідають документу
    5. [Поверніть акцизні марки постачальнику (АЕД №4)](aed/aed4-povernennia.md)
    6. [Додайте нового контрагента ЕО](dovidnyky/dodaty-kontragenta-eo.md)

=== "Розробник"

    <p class="role-lead">Програміст BAS або касового ПЗ: вбудовуєте AEDOC у свою конфігурацію чи підключаєте касу.</p>

    1. [Технічна документація](integratsiia/itdeptinfo.md): вимоги до платформи, служба підпису, ліцензування, інтеграція з об'єктами вашої конфігурації і введення на підставі
    2. [Зберігання даних](integratsiia/zberigannia/index.md): приріст бази і зовнішнє сховище MS SQL
    3. [HTTP-сервіс «Сховище марок» для ПРРО](integratsiia/skhovyshche-marok/index.md) і [API для касового ПЗ](integratsiia/skhovyshche-marok/rozrobnykam.md)
    4. Розгорніть standalone-конфігурацію для тестів і пройдіть [повний цикл з відео](testuvannia/index.md)

=== "Аналітик"

    <p class="role-lead">Продакт-менеджер чи аналітик: оцінюєте, як AEDOC закриє процеси вашого бізнесу.</p>

    1. Подивіться [відео тестів](testuvannia/index.md) — як виглядає цикл від АЕД до чека
    2. [Технічна документація](integratsiia/itdeptinfo.md): схеми для роздрібної мережі, імпорту та опту
    3. [Тест навантаження](integratsiia/zberigannia/testuvannia.md): скільки займають 1000 АЕД і 1 млн марок
    4. [Сховище марок](integratsiia/skhovyshche-marok/index.md) — для мереж з кількома касами
    5. Пройдіться по [інструкціях роботи з АЕД](aed/index.md) — так виглядатиме щоденна робота користувачів

## Розділи довідки

<div class="cards" markdown>

<a class="card" href="integratsiia/">
<strong>Інтеграція</strong>
<span>Для ІТ і продакт-менеджерів: вимоги, типові рішення, зберігання даних, сховище марок.</span>
</a>

<a class="card" href="navchannia/">
<strong>Навчання роботи з АЕДок</strong>
<span>Перший запуск, робота з АЕД, довідники — покрокові інструкції зі скріншотами.</span>
</a>

<a class="card card--dev" href="testuvannia/">
<strong>Тестування</strong>
<span>Відео тестів інтеграції з різними конфігураціями в тестовому середовищі еАкциз.</span>
</a>

</div>

<p class="home-footer">AEDOC розробляє WebCheck — розробка для облікових систем з 2008 року, ПРРО — з 2020. Деталі — на <a href="https://aedoc.com.ua">aedoc.com.ua</a>.</p>
