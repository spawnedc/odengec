<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>{% block page_title %}{% endblock %} - Ödengeç</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ STATIC_URL }}css/styles.css">
  </head>
  <body>
    <header>
      <div class="container">
        <nav class="navbar">
          <div class="navbar-inner">
            <a class="brand" href="{% url 'dashboard' %}">{{ APP_TITLE }}</a>
            <ul class="nav">
              <li{% if section == 'dashboard' %} class="active"{% endif %}><a href="{% url 'dashboard' %}">Dashboard</a></li>
              <li{% if section == 'create_payment' %} class="active"{% endif %}><a href="{% url 'create_payment' %}">Create Payment</a></li>
            </ul>
          </div>
        </nav>
      </div>
    </header>

    <div class="content">
      <div class="container">{% block content %}{% endblock %}</div>
    </div>

    <footer>
      <div class="container">
        <p>Ödengeç, &copy; 2016, Can Yilmaz. <small>There is no copyright really, but looks cool :P</small></p>
      </div>
    </footer>

    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.5.8/angular.min.js"></script>
  </body>
</html>
