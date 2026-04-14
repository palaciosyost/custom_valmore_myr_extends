from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cargo = fields.Selection([
        ('gerencia_direccion', 'Gerencia / Dirección'),
        ('finanzas', 'Finanzas'),
        ('operaciones', 'Operaciones'),
        ('administracion', 'Administración'),
        ('comercial', 'Comercial'),
        ('tecnico', 'Técnico'),
        ('logistica', 'Logística'),
        ('compras', 'Compras'),
        ('legal', 'Legal'),
        ('otro', 'Otro')
    ], string='Cargo')
    tipo_comprobante = fields.Selection([
        ('01', '01 Factura'),
        ('02', '02 Recibo de Honorarios'),
        ('03', '03 Boleta de Venta'),
        ('05', '05 Boleto de Avión'),
        ('07', '07 Nota de Crédito'),
        ('08', '08 Nota de Débito'),
        ('10', '10 Recibo Arrendamiento'),
        ('12', '12 Ticket Maquina Registradora'),
        ('14', '14 Recibo Servicios Públicos'),
        ('00', '00 Otros')
    ], string='Tipo de Comprobante')
    tamanio_empresa = fields.Selection([
        ('gran_empresa', 'Gran Empresa'),
        ('mediana_empresa', 'Mediana Empresa'),
        ('pequena_empresa', 'Pequeña Empresa'),
        ('microempresa', 'Microempresa'),
        ('entidad_publica', 'Entidad Pública'),
        ('banco_financiera', 'Banco / Financiera'),
        ('ong', 'ONG'),
    ], string='Tamaño de Empresa')

    segmentacion = fields.Selection([
        ('a_estrategico', 'A - Estratégico'),
        ('b_recurrente', 'B - Recurrente'),
        ('c_ocasional', 'C - Ocasional'),
    ], string='Segmentación')
    linea_negocio = fields.Selection([
        ('INM', 'Inmuebles'),
        ('MAQ', 'Maquinaria y Equipo'),
        ('VEH', 'Vehículos'),
        ('INV', 'Inventarios'),
        ('MER', 'Merma'),
        ('EMP', 'Valorización de empresas en marcha'),
        ('ESP', 'Servicios especiales / Atípicos'),
    ], string='Línea de Negocio')    
    cliente_recurrente = fields.Boolean(string='Cliente recurrente')
    rol_decision = fields.Selection([
        ("Decisor" , "Decisor"),
        ("Influenciador" , "Influenciador"),
        ("Técnico" , "Técnico"),
        ("Administrador" , "Administrador"),
        ("Usuario" , "Usuario"),
        ("Contacto operativo" , "Contacto operativo")], string="Rol de decisiones")