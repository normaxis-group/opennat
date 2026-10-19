# Utilitaire de calcul OpenNAT (opennat.utilitaire) dans un conteneur minimal, sans LibreOffice : la fiche de synthèse
# sort en Word, pas en PDF. L'utilitaire n'a pas de compte : ne publier le port que sur la machine (127.0.0.1).
#   docker build -t opennat .
#   docker run --rm -p 127.0.0.1:8770:8770 -v /chemin/resultats:/travail opennat
#   docker run --rm -v /chemin/etude:/travail opennat python -m opennat calcul /travail/projet.json --sortie /travail
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY opennat ./opennat
COPY donnees ./donnees
COPY schemas ./schemas
COPY banc ./banc
COPY methode/conventions.md ./methode/
RUN pip install --no-cache-dir numpy lxml python-docx
ENV OPENNAT_HOTE=0.0.0.0 PYTHONUNBUFFERED=1
EXPOSE 8770
CMD ["python", "-m", "opennat.utilitaire", "--sans-navigateur", "--dossier", "/travail"]
