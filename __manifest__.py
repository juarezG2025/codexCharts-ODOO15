{
    'name': 'codex catalogo custom y tipo de documentos',
    'summary': """
        Plan de cuentas para modificado.""",
    'version': '1.0',
    'category': 'Localization',
    'description': """
agregar nomenglatura de cuentas contables en catalogo .""",
    'author': 'codex developer',
    'website': 'http://www.codex.com/',
    'depends': ['base', 'account'],
    'data': [
        'data/codex_chart_data.xml',
        'data/account_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_fiscal_position_tax_template_data.xml',
        #Es importante que la llamada a la funcion try_loading_for_current_company este por ultimo, despues de todos los archivos
        #que definen impuestos, cuentas o posiciones fiscales,si dejo alguno despues de la llamada, no se crea cuando se aplique
        #la localizacion
        'data/account_chart_template_configure_data.xml'
    ],
}
