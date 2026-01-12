from swagger_coverage_tool import SwaggerCoverageTracker

# Инициализация трекера для  сервиса
# 'api-course' должен точно совпадать с ключом `key` в SWAGGER_COVERAGE_SERVICES
tracker = SwaggerCoverageTracker(service="api-course")