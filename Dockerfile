# Utilitaire de calcul OpenNAT (opennat.utilitaire) dans un conteneur minimal, sans LibreOffice : la fiche de synthèse
# sort en Word, pas en PDF. L'utilitaire n'a pas de compte : ne publier le port que sur la machine (127.0.0.1).
#   docker build -t opennat .
#   docker run --rm -p 127.0.0.1:8770:8770 -v /chemin/resultats:/travail opennat
#   docker run --rm -v /chemin/etude:/travail opennat python -m opennat calcul /travail/projet.json --sortie /travail
# Version en ligne (opennat.irice-certification.com) : variable OPENNAT_PUBLIC=1 (identifiants aléatoires, limites,
# purge des résultats après 24 heures, en-têtes de sécurité ; voir opennat/utilitaire/serveur.py).
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY opennat ./opennat
COPY donnees ./donnees
COPY schemas ./schemas
COPY banc ./banc
COPY methode/conventions.md ./methode/
RUN pip install --no-cache-dir numpy lxml python-docx
RUN useradd --create-home --uid 10001 opennat && mkdir -p /travail && chown opennat /travail
USER opennat
ENV OPENNAT_HOTE=0.0.0.0 PYTHONUNBUFFERED=1
EXPOSE 8770
CMD ["python", "-m", "opennat.utilitaire", "--sans-navigateur", "--dossier", "/travail"]
