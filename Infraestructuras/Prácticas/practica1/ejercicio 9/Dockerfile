FROM python:3.9-slim

# Crear directorio como root
RUN mkdir -p /app/logs && chmod 755 /app/logs

WORKDIR /app

RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY writer_app.py .

RUN chown -R appuser:appuser /app

# Cambiar a usuario no-root para seguridad
USER appuser

CMD ["python", "-u", "writer_app.py"]