# Subir una carpeta a GitHub desde Visual Studio Code

Guía paso a paso para subir una carpeta (o varias) a GitHub usando Visual Studio Code.

---

## 0. Configuración inicial (solo la primera vez)

### Paso 1: Iniciar sesión en GitHub
Ve a [https://github.com/](https://github.com/) e inicia sesión con tu cuenta.

### Paso 2: Verificar la sesión de Git en Visual Studio Code
En la parte inferior izquierda de VS Code hay un ícono con forma de perfil. Haz clic ahí y revisa si hay otra cuenta con la sesión abierta. Si es así:
1. Haz clic sobre la cuenta.
2. Selecciona **Sign out**.

### Paso 3: Abrir la terminal
En la barra superior: **Terminal → New Terminal**.

### Paso 4: Configurar tu usuario de Git
Escribe estos comandos en la terminal (reemplazando los valores):

```bash
git config --global user.name "nombreUsuario"
git config --global user.email "correoUsuario"
```

> 💡 **¿Dónde encuentro mi nombre de usuario?** En GitHub, arriba a la derecha, haz clic en tu foto de perfil → **Your profile**. El nombre que aparece ahí es tu `nombreUsuario`.
> Usa el mismo correo con el que te registraste en GitHub.

### Paso 5: Definir VS Code como editor de Git

```bash
git config --global core.editor "code --wait"
```

---

## 1. Subir la carpeta a GitHub por primera vez

### Paso 1: Abrir Control de versiones (Source Control)
En la barra lateral izquierda, haz clic en el ícono debajo de la lupa (**Source Control**), o usa el atajo:

```
Ctrl + Shift + G
```

### Paso 2: Inicializar el repositorio
Haz clic en **Initialize Repository**.

> ⚠️ Si no aparece esa opción, es porque la carpeta ya tiene un repositorio Git asociado. Borra la carpeta oculta `.git` dentro de la carpeta (o carpetas) que vas a subir, y vuelve a intentarlo.

### Paso 3: Hacer el primer commit
1. Escribe un **mensaje obligatorio** describiendo qué se hizo (por ejemplo: *"Primera versión del proyecto"*).
2. Haz clic en **Commit**.

> Si aparece una ventana indicando que no hay archivos en *staged* y preguntando si deseas incluirlos directamente, haz clic en **Yes**.

### Paso 4: Publicar la rama
Haz clic en **Publish Branch**.

- Se abrirá una ventana externa para iniciar sesión en GitHub (correo y contraseña). Al terminar, volverás automáticamente a VS Code.
- Luego te preguntará si el repositorio debe ser **público** o **privado**. Selecciona **Public** (o **Private** según lo que necesites).

### Paso 5: Verificar en GitHub
Tus archivos ya estarán en GitHub. Para verlos: arriba a la derecha, haz clic en tu foto de perfil → **Your repositories**.

---

## 2. Subir cambios después de la primera vez

Una vez que el repositorio ya fue publicado, el botón **Publish Branch** ya no aparecerá. En su lugar verás el botón **Sync Changes**.

Cada vez que hagas cambios en tu código:
1. Repite el **Paso 3** (mensaje + commit).
2. Haz clic en **Sync Changes** para subir los cambios a GitHub.