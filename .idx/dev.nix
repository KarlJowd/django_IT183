{pkgs}: {
  channel = "stable-24.05";
  packages = [
    pkgs.python312
  ];
  idx.extensions = [
    "ms-python.python"
  ];
  idx.workspace.onCreate = {
    create-venv = "python -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/python manage.py migrate";
  };
  idx.previews = {
    previews = {
      web = {
        command = [
          "sh"
          "-c"
          "if [ ! -d .venv ]; then python -m venv .venv && .venv/bin/pip install -r requirements.txt; fi && .venv/bin/python manage.py migrate --noinput && .venv/bin/python manage.py runserver 0.0.0.0:$PORT --noreload --insecure"
        ];
        manager = "web";
      };
    };
  };
}
