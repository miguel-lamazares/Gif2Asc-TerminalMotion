"""
PNGPersonalizer.py - Camada de personalização direta de frames PNG
Permite aplicar efeitos, ajustes e transformações nos frames antes da conversão ASCII
"""

import os
import json
import shutil
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageFont
from TerminalLib import Terminal as ter
from TerminalLib import asc
import sys

class PNGCustomizer:
    def __init__(self):
        self.config = {}
        self.effects_stack = []  # Pilha de efeitos a aplicar
        self.batch_mode = True   # Modo batch para todos os frames
        
    def show_menu(self):
        """Menu principal de personalização"""
        ter.Clear_all()
        ter.print_centralizedText(ter.Colors.PURPLE + "╔══════════════════════════════════════╗")
        ter.print_centralizedText(ter.Colors.PURPLE + "║    PERSONALIZADOR DE FRAMES PNG      ║")
        ter.print_centralizedText(ter.Colors.PURPLE + "╚══════════════════════════════════════╝\n")
        
        while True:
            ter.typewrite(ter.Colors.CYAN + "Efeitos Disponíveis:\n\n", 0.02)
            ter.typewrite(ter.Colors.YELLOW + "1.  Ajustes Básicos (Brilho/Contraste/Saturação)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "2.  Filtros e Efeitos (Blur, Sharpen, Edge)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "3.  Transformações (Rotação, Flip, Crop)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "4.  Correção de Cores (Balanço, Temperatura)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "5.  Adicionar Overlays (Texto, Logos, Bordas)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "6.  Efeitos Artísticos (Sépia, Preto e Branco)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "7.  Redimensionamento Inteligente\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "8.  Correção de GIF (Remover fundo, otimizar)\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "9.  Aplicar a TODOS os frames\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "10. Aplicar a FRAME ESPECÍFICO\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "11. Visualizar efeitos\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "12. Salvar configuração\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "13. Carregar configuração\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "14. Processar e Aplicar TUDO\n", 0.01)
            ter.typewrite(ter.Colors.YELLOW + "15. Sair\n\n", 0.01)
            
            choice = ter.read_int(1, 15)
            
            if choice == 1:
                self.basic_adjustments()
            elif choice == 2:
                self.filter_effects()
            elif choice == 3:
                self.transformations()
            elif choice == 4:
                self.color_correction()
            elif choice == 5:
                self.overlay_effects()
            elif choice == 6:
                self.artistic_effects()
            elif choice == 7:
                self.smart_resize()
            elif choice == 8:
                self.gif_optimization()
            elif choice == 9:
                self.apply_to_all_frames()
            elif choice == 10:
                self.apply_to_specific_frame()
            elif choice == 11:
                self.preview_effects()
            elif choice == 12:
                self.save_configuration()
            elif choice == 13:
                self.load_configuration()
            elif choice == 14:
                self.process_all()
                break
            elif choice == 15:
                ter.typewrite(ter.Colors.RED + "Saindo sem aplicar...\n", 0.02)
                sys.exit(0)
    
    def basic_adjustments(self):
        """Ajustes básicos de imagem"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== AJUSTES BÁSICOS ===\n\n", 0.02)
        
        # Brilho
        ter.typewrite(ter.Colors.YELLOW + "Brilho (0.0 - 3.0, padrão=1.0): ", 0.02)
        brightness = float(input() or "1.0")
        
        # Contraste
        ter.typewrite(ter.Colors.YELLOW + "Contraste (0.0 - 3.0, padrão=1.0): ", 0.02)
        contrast = float(input() or "1.0")
        
        # Saturação
        ter.typewrite(ter.Colors.YELLOW + "Saturação (0.0 - 3.0, padrão=1.0): ", 0.02)
        saturation = float(input() or "1.0")
        
        # Nitidez
        ter.typewrite(ter.Colors.YELLOW + "Nitidez (0.0 - 3.0, padrão=1.0): ", 0.02)
        sharpness = float(input() or "1.0")
        
        self.effects_stack.append({
            'type': 'basic_adjustments',
            'brightness': brightness,
            'contrast': contrast,
            'saturation': saturation,
            'sharpness': sharpness
        })
        
        ter.typewrite(ter.Colors.GREEN + "✓ Ajustes adicionados à pilha!\n", 0.02)
    
    def filter_effects(self):
        """Filtros e efeitos especiais"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== FILTROS E EFEITOS ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Blur (Suavização)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Sharpen (Nitidez)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Contour (Contorno)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Detail (Detalhes)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Edge Enhance (Bordas)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "6. Emboss (Relevo)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "7. Smooth (Suave)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "8. Gaussian Blur\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "9. Median Filter\n\n", 0.01)
        
        choice = ter.read_int(1, 9)
        
        filters_map = {
            1: ('BLUR', 1),
            2: ('SHARPEN', 1),
            3: ('CONTOUR', 1),
            4: ('DETAIL', 1),
            5: ('EDGE_ENHANCE', 1),
            6: ('EMBOSS', 1),
            7: ('SMOOTH', 1),
            8: ('GAUSSIAN_BLUR', 2),
            9: ('MEDIAN_FILTER', 3)
        }
        
        filter_name, needs_param = filters_map[choice]
        
        intensity = 1
        if needs_param == 2:  # Gaussian Blur
            ter.typewrite(ter.Colors.YELLOW + "Raio (1-10): ", 0.02)
            intensity = int(input() or "2")
        elif needs_param == 3:  # Median Filter
            ter.typewrite(ter.Colors.YELLOW + "Tamanho (1-10): ", 0.02)
            intensity = int(input() or "3")
        
        self.effects_stack.append({
            'type': 'filter',
            'filter': filter_name,
            'intensity': intensity
        })
        
        ter.typewrite(ter.Colors.GREEN + f"✓ Filtro '{filter_name}' adicionado!\n", 0.02)
    
    def transformations(self):
        """Transformações geométricas"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== TRANSFORMAÇÕES ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Rotacionar\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Flip Horizontal\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Flip Vertical\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Transpor\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Crop (Recortar)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "6. Espelhar\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "7. Ajustar Perspectiva\n\n", 0.01)
        
        choice = ter.read_int(1, 7)
        
        if choice == 1:  # Rotação
            ter.typewrite(ter.Colors.YELLOW + "Ângulo (graus): ", 0.02)
            angle = float(input() or "0")
            expand = ter.read_int(1, 2, "Expandir imagem? (1-Sim/2-Não): ") == 1
            
            self.effects_stack.append({
                'type': 'rotate',
                'angle': angle,
                'expand': expand
            })
            
        elif choice in [2, 3, 4, 6]:  # Flips e transposição
            transforms = {
                2: 'FLIP_LEFT_RIGHT',
                3: 'FLIP_TOP_BOTTOM',
                4: 'TRANSPOSE',
                6: 'MIRROR'
            }
            
            self.effects_stack.append({
                'type': 'transform',
                'transform': transforms[choice]
            })
            
        elif choice == 5:  # Crop
            ter.typewrite(ter.Colors.YELLOW + "Crop - coordenadas (esquerda, topo, direita, baixo)\n", 0.02)
            ter.typewrite("Exemplo: 10 10 200 150\n", 0.02)
            coords = input("Coordenadas: ").split()
            if len(coords) == 4:
                left, top, right, bottom = map(int, coords)
                self.effects_stack.append({
                    'type': 'crop',
                    'coords': [left, top, right, bottom]
                })
                
        elif choice == 7:  # Perspectiva
            ter.typewrite(ter.Colors.YELLOW + "Ajuste de perspectiva - pontos de origem e destino\n", 0.02)
            # Implementação simplificada
            self.effects_stack.append({
                'type': 'perspective',
                'strength': 0.1
            })
        
        ter.typewrite(ter.Colors.GREEN + "✓ Transformação adicionada!\n", 0.02)
    
    def color_correction(self):
        """Correção avançada de cores"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== CORREÇÃO DE CORES ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Ajustar Balanço de Cores\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Temperatura de Cor\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Matiz/Saturação\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Níveis (Histograma)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Curvas\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "6. Equalização\n\n", 0.01)
        
        choice = ter.read_int(1, 6)
        
        if choice == 1:  # Balanço de cores
            ter.typewrite("Ajuste R/G/B (-100 a 100):\n", 0.02)
            red = int(input("Vermelho: ") or "0")
            green = int(input("Verde: ") or "0")
            blue = int(input("Azul: ") or "0")
            
            self.effects_stack.append({
                'type': 'color_balance',
                'red': red / 100.0,
                'green': green / 100.0,
                'blue': blue / 100.0
            })
            
        elif choice == 2:  # Temperatura
            ter.typewrite(ter.Colors.YELLOW + "Temperatura (-100 frio/azul a 100 quente/vermelho): ", 0.02)
            temp = int(input() or "0")
            
            self.effects_stack.append({
                'type': 'temperature',
                'value': temp / 100.0
            })
            
        elif choice == 3:  # Matiz/Saturação
            ter.typewrite("Matiz (-180 a 180): ", 0.02)
            hue = int(input() or "0")
            ter.typewrite("Saturação (-100 a 100): ", 0.02)
            sat = int(input() or "0")
            
            self.effects_stack.append({
                'type': 'hue_saturation',
                'hue': hue,
                'saturation': sat / 100.0
            })
            
        elif choice == 4:  # Níveis
            ter.typewrite("Ponto preto (0-255): ", 0.02)
            black = int(input() or "0")
            ter.typewrite("Ponto cinza (0-255): ", 0.02)
            gray = int(input() or "128")
            ter.typewrite("Ponto branco (0-255): ", 0.02)
            white = int(input() or "255")
            
            self.effects_stack.append({
                'type': 'levels',
                'black_point': black,
                'gray_point': gray,
                'white_point': white
            })
            
        elif choice == 5:  # Curvas (simplificado)
            ter.typewrite(ter.Colors.YELLOW + "Tipo de curva (1-S, 2-Linear, 3-Invertida): ", 0.02)
            curve_type = ter.read_int(1, 3)
            
            self.effects_stack.append({
                'type': 'curves',
                'curve_type': curve_type
            })
            
        elif choice == 6:  # Equalização
            self.effects_stack.append({
                'type': 'equalize'
            })
        
        ter.typewrite(ter.Colors.GREEN + "✓ Correção de cores adicionada!\n", 0.02)
    
    def overlay_effects(self):
        """Adicionar overlays (texto, logos, bordas)"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== OVERLAYS ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Adicionar Texto\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Adicionar Logo/Marca d'água\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Adicionar Borda\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Adicionar Overlay de Cor\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Adicionar Gradiente\n\n", 0.01)
        
        choice = ter.read_int(1, 5)
        
        if choice == 1:  # Texto
            ter.typewrite("Texto: ", 0.02)
            text = input()
            ter.typewrite("Posição (1-Top, 2-Center, 3-Bottom): ", 0.02)
            position = ter.read_int(1, 3)
            ter.typewrite("Cor (ex: #FF0000 ou red): ", 0.02)
            color = input() or "#FFFFFF"
            ter.typewrite("Tamanho da fonte (10-100): ", 0.02)
            size = int(input() or "20")
            
            self.effects_stack.append({
                'type': 'text_overlay',
                'text': text,
                'position': position,
                'color': color,
                'size': size
            })
            
        elif choice == 2:  # Logo
            ter.typewrite("Caminho da imagem da logo: ", 0.02)
            logo_path = input()
            ter.typewrite("Opacidade (0-100): ", 0.02)
            opacity = int(input() or "50")
            ter.typewrite("Posição (1-TL, 2-TR, 3-BL, 4-BR, 5-Center): ", 0.02)
            position = ter.read_int(1, 5)
            
            self.effects_stack.append({
                'type': 'logo_overlay',
                'path': logo_path,
                'opacity': opacity / 100.0,
                'position': position
            })
            
        elif choice == 3:  # Borda
            ter.typewrite("Espessura da borda (px): ", 0.02)
            thickness = int(input() or "5")
            ter.typewrite("Cor da borda: ", 0.02)
            color = input() or "#000000"
            ter.typewrite("Estilo (1-Solida, 2-Pontilhada, 3-Arredondada): ", 0.02)
            style = ter.read_int(1, 3)
            
            self.effects_stack.append({
                'type': 'border',
                'thickness': thickness,
                'color': color,
                'style': style
            })
            
        elif choice == 4:  # Overlay de cor
            ter.typewrite("Cor (ex: #FF000080 para vermelho semi-transparente): ", 0.02)
            color = input() or "#00000080"
            ter.typewrite("Modo de mistura (1-Normal, 2-Multiply, 3-Overlay): ", 0.02)
            blend_mode = ter.read_int(1, 3)
            
            self.effects_stack.append({
                'type': 'color_overlay',
                'color': color,
                'blend_mode': blend_mode
            })
            
        elif choice == 5:  # Gradiente
            ter.typewrite("Cor inicial: ", 0.02)
            color1 = input() or "#000000"
            ter.typewrite("Cor final: ", 0.02)
            color2 = input() or "#FFFFFF"
            ter.typewrite("Direção (1-Horizontal, 2-Vertical, 3-Diagonal): ", 0.02)
            direction = ter.read_int(1, 3)
            ter.typewrite("Opacidade (0-100): ", 0.02)
            opacity = int(input() or "30")
            
            self.effects_stack.append({
                'type': 'gradient',
                'color1': color1,
                'color2': color2,
                'direction': direction,
                'opacity': opacity / 100.0
            })
        
        ter.typewrite(ter.Colors.GREEN + "✓ Overlay adicionado!\n", 0.02)
    
    def artistic_effects(self):
        """Efeitos artísticos"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== EFEITOS ARTÍSTICOS ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Sépia\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Preto e Branco\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Posterizar\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Solarizar\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Desenho\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "6. Pintura a Óleo\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "7. Pixel Art\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "8. Vignette\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "9. Granulado (Filme)\n\n", 0.01)
        
        choice = ter.read_int(1, 9)
        
        effects_map = {
            1: ('sepia', 0),
            2: ('grayscale', 0),
            3: ('posterize', 1),
            4: ('solarize', 1),
            5: ('sketch', 1),
            6: ('oil_painting', 1),
            7: ('pixelate', 1),
            8: ('vignette', 2),
            9: ('film_grain', 1)
        }
        
        effect_name, needs_param = effects_map[choice]
        
        intensity = 4  # Valor padrão
        if needs_param == 1:
            ter.typewrite(ter.Colors.YELLOW + "Intensidade (1-10): ", 0.02)
            intensity = int(input() or "4")
        elif needs_param == 2:
            ter.typewrite(ter.Colors.YELLOW + "Força do vignette (1-20): ", 0.02)
            intensity = int(input() or "10")
        
        self.effects_stack.append({
            'type': 'artistic',
            'effect': effect_name,
            'intensity': intensity
        })
        
        ter.typewrite(ter.Colors.GREEN + f"✓ Efeito '{effect_name}' adicionado!\n", 0.02)
    
    def smart_resize(self):
        """Redimensionamento inteligente"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== REDIMENSIONAMENTO INTELIGENTE ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Manter Aspecto\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Preencher (Crop)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Esticar\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Redimensionar para Terminal\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Redimensionar para ASCII (80 colunas)\n\n", 0.01)
        
        choice = ter.read_int(1, 5)
        
        if choice in [1, 2, 3]:  # Redimensionamento normal
            ter.typewrite("Largura (px): ", 0.02)
            width = int(input())
            ter.typewrite("Altura (px): ", 0.02)
            height = int(input())
            
            methods = {1: 'keep_aspect', 2: 'crop_fill', 3: 'stretch'}
            
            self.effects_stack.append({
                'type': 'resize',
                'width': width,
                'height': height,
                'method': methods[choice]
            })
            
        elif choice == 4:  # Para terminal
            import shutil
            term_size = shutil.get_terminal_size()
            self.effects_stack.append({
                'type': 'resize_terminal',
                'columns': term_size.columns,
                'lines': term_size.lines
            })
            
        elif choice == 5:  # Para ASCII
            ter.typewrite("Largura em caracteres (padrão=80): ", 0.02)
            width = int(input() or "80")
            
            self.effects_stack.append({
                'type': 'resize_ascii',
                'width': width
            })
        
        ter.typewrite(ter.Colors.GREEN + "✓ Redimensionamento configurado!\n", 0.02)
    
    def gif_optimization(self):
        """Otimização específica para GIFs"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== OTIMIZAÇÃO PARA GIF ===\n\n", 0.02)
        
        ter.typewrite(ter.Colors.YELLOW + "1. Remover Fundo (Chromakey)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "2. Reduzir Cores (Palette)\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "3. Otimizar Transparência\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "4. Remover Frames Duplicados\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "5. Suavizar Transições\n", 0.01)
        ter.typewrite(ter.Colors.YELLOW + "6. Corrigir Piscamento\n\n", 0.01)
        
        choice = ter.read_int(1, 6)
        
        if choice == 1:  # Chromakey
            ter.typewrite("Cor do fundo para remover (ex: #00FF00): ", 0.02)
            color = input() or "#00FF00"
            ter.typewrite("Tolerância (0-100): ", 0.02)
            tolerance = int(input() or "10")
            
            self.effects_stack.append({
                'type': 'chromakey',
                'color': color,
                'tolerance': tolerance
            })
            
        elif choice == 2:  # Reduzir cores
            ter.typewrite("Número máximo de cores (2-256): ", 0.02)
            colors = int(input() or "256")
            
            self.effects_stack.append({
                'type': 'reduce_colors',
                'max_colors': colors
            })
            
        elif choice == 3:  # Otimizar transparência
            self.effects_stack.append({
                'type': 'optimize_transparency'
            })
            
        elif choice == 4:  # Remover frames duplicados
            ter.typewrite("Similaridade mínima para remover (0-100): ", 0.02)
            similarity = int(input() or "95")
            
            self.effects_stack.append({
                'type': 'remove_duplicates',
                'similarity': similarity
            })
            
        elif choice == 5:  # Suavizar transições
            ter.typewrite("Força da suavização (1-10): ", 0.02)
            strength = int(input() or "3")
            
            self.effects_stack.append({
                'type': 'smooth_transitions',
                'strength': strength
            })
            
        elif choice == 6:  # Corrigir piscamento
            self.effects_stack.append({
                'type': 'fix_flicker'
            })
        
        ter.typewrite(ter.Colors.GREEN + "✓ Otimização configurada!\n", 0.02)
    
    def apply_effect(self, image, effect):
        """Aplica um efeito individual a uma imagem"""
        from PIL import ImageChops
        
        effect_type = effect['type']
        
        try:
            if effect_type == 'basic_adjustments':
                # Brilho
                if effect['brightness'] != 1.0:
                    enhancer = ImageEnhance.Brightness(image)
                    image = enhancer.enhance(effect['brightness'])
                
                # Contraste
                if effect['contrast'] != 1.0:
                    enhancer = ImageEnhance.Contrast(image)
                    image = enhancer.enhance(effect['contrast'])
                
                # Saturação
                if effect['saturation'] != 1.0:
                    if image.mode != 'RGB' and image.mode != 'RGBA':
                        image = image.convert('RGB')
                    enhancer = ImageEnhance.Color(image)
                    image = enhancer.enhance(effect['saturation'])
                
                # Nitidez
                if effect['sharpness'] != 1.0:
                    enhancer = ImageEnhance.Sharpness(image)
                    image = enhancer.enhance(effect['sharpness'])
            
            elif effect_type == 'filter':
                filter_map = {
                    'BLUR': ImageFilter.BLUR,
                    'SHARPEN': ImageFilter.SHARPEN,
                    'CONTOUR': ImageFilter.CONTOUR,
                    'DETAIL': ImageFilter.DETAIL,
                    'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
                    'EMBOSS': ImageFilter.EMBOSS,
                    'SMOOTH': ImageFilter.SMOOTH,
                    'SMOOTH_MORE': ImageFilter.SMOOTH_MORE
                }
                
                if effect['filter'] == 'GAUSSIAN_BLUR':
                    image = image.filter(ImageFilter.GaussianBlur(effect['intensity']))
                elif effect['filter'] == 'MEDIAN_FILTER':
                    image = image.filter(ImageFilter.MedianFilter(effect['intensity']))
                elif effect['filter'] in filter_map:
                    image = image.filter(filter_map[effect['filter']])
            
            elif effect_type == 'rotate':
                image = image.rotate(effect['angle'], 
                                    expand=effect.get('expand', False),
                                    resample=Image.Resampling.BICUBIC)
            
            elif effect_type == 'transform':
                transform_map = {
                    'FLIP_LEFT_RIGHT': Image.FLIP_LEFT_RIGHT,
                    'FLIP_TOP_BOTTOM': Image.FLIP_TOP_BOTTOM,
                    'TRANSPOSE': Image.TRANSPOSE,
                    'MIRROR': Image.FLIP_LEFT_RIGHT
                }
                if effect['transform'] in transform_map:
                    image = image.transpose(transform_map[effect['transform']])
            
            elif effect_type == 'crop':
                left, top, right, bottom = effect['coords']
                image = image.crop((left, top, right, bottom))
            
            elif effect_type == 'color_balance':
                # Simulação de balanço de cores
                r, g, b = image.split() if image.mode == 'RGB' else image.convert('RGB').split()
                
                if 'red' in effect:
                    r = r.point(lambda i: min(255, i * (1 + effect['red'])))
                if 'green' in effect:
                    g = g.point(lambda i: min(255, i * (1 + effect['green'])))
                if 'blue' in effect:
                    b = b.point(lambda i: min(255, i * (1 + effect['blue'])))
                
                image = Image.merge('RGB', (r, g, b))
            
            elif effect_type == 'hue_saturation':
                if image.mode != 'HSV':
                    image = image.convert('HSV')
                
                h, s, v = image.split()
                
                # Ajustar matiz
                if 'hue' in effect:
                    h = h.point(lambda i: (i + effect['hue']) % 256)
                
                # Ajustar saturação
                if 'saturation' in effect:
                    s = s.point(lambda i: min(255, i * (1 + effect['saturation'])))
                
                image = Image.merge('HSV', (h, s, v)).convert('RGB')
            
            elif effect_type == 'text_overlay':
                draw = ImageDraw.Draw(image)
                
                # Carregar fonte (simplificado)
                try:
                    font = ImageFont.truetype("arial.ttf", effect['size'])
                except:
                    font = ImageFont.load_default()
                
                # Calcular posição
                text_bbox = draw.textbbox((0, 0), effect['text'], font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                positions = {
                    1: (10, 10),  # Top
                    2: ((image.width - text_width) // 2, (image.height - text_height) // 2),  # Center
                    3: (10, image.height - text_height - 10)  # Bottom
                }
                
                position = positions.get(effect['position'], (10, 10))
                
                # Desenhar texto
                draw.text(position, effect['text'], font=font, fill=effect['color'])
            
            elif effect_type == 'border':
                draw = ImageDraw.Draw(image)
                width, height = image.size
                
                # Desenhar borda
                if effect['style'] == 1:  # Sólida
                    draw.rectangle([(0, 0), (width-1, height-1)], 
                                 outline=effect['color'], 
                                 width=effect['thickness'])
                elif effect['style'] == 2:  # Pontilhada (simplificado)
                    for i in range(0, width, 10):
                        draw.line([(i, 0), (i+5, 0)], fill=effect['color'], width=effect['thickness'])
            
            elif effect_type == 'artistic':
                if effect['effect'] == 'sepia':
                    # Converter para sépia
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    sepia_filter = np.array([[0.393, 0.769, 0.189],
                                            [0.349, 0.686, 0.168],
                                            [0.272, 0.534, 0.131]])
                    
                    img_array = np.array(image).astype(np.float32)
                    img_array = np.dot(img_array, sepia_filter.T)
                    img_array = np.clip(img_array, 0, 255).astype(np.uint8)
                    image = Image.fromarray(img_array)
                
                elif effect['effect'] == 'grayscale':
                    image = ImageOps.grayscale(image)
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                
                elif effect['effect'] == 'posterize':
                    image = ImageOps.posterize(image, effect['intensity'])
                
                elif effect['effect'] == 'solarize':
                    image = ImageOps.solarize(image, 
                                            threshold=255 - (effect['intensity'] * 25))
            
            elif effect_type == 'resize':
                width, height = effect['width'], effect['height']
                method = effect['method']
                
                if method == 'keep_aspect':
                    # Manter aspecto, redimensionar para caber
                    image.thumbnail((width, height), Image.Resampling.LANCZOS)
                elif method == 'crop_fill':
                    # Redimensionar e cortar
                    image.thumbnail((width, height), Image.Resampling.LANCZOS)
                    # Centralizar e cortar
                    left = (image.width - width) // 2
                    top = (image.height - height) // 2
                    right = left + width
                    bottom = top + height
                    image = image.crop((left, top, right, bottom))
                elif method == 'stretch':
                    image = image.resize((width, height), Image.Resampling.LANCZOS)
            
            elif effect_type == 'resize_ascii':
                width = effect['width']
                # Calcular altura mantendo proporção para ASCII
                ratio = image.height / image.width
                height = int(width * ratio * 0.5)  # Fator 0.5 para caracteres
                image = image.resize((width, height), Image.Resampling.LANCZOS)
            
            elif effect_type == 'chromakey':
                # Remover fundo verde (simplificado)
                if image.mode != 'RGBA':
                    image = image.convert('RGBA')
                
                data = np.array(image)
                red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
                
                # Criar máscara para cor específica
                mask = ((red > 200) & (green > 200) & (blue < 100))
                data[:,:,3] = np.where(mask, 0, alpha)
                
                image = Image.fromarray(data)
            
            elif effect_type == 'reduce_colors':
                # Reduzir paleta de cores
                image = image.convert('P', palette=Image.Palette.ADAPTIVE, 
                                    colors=effect['max_colors'])
                image = image.convert('RGB')
        
        except Exception as e:
            ter.typewrite(ter.Colors.RED + f"Erro ao aplicar efeito {effect_type}: {e}\n", 0.02)
        
        return image
    
    def apply_to_all_frames(self):
        """Configura para aplicar a todos os frames"""
        self.batch_mode = True
        ter.typewrite(ter.Colors.GREEN + "✓ Modo BATCH ativado - efeitos serão aplicados a TODOS os frames\n", 0.02)
    
    def apply_to_specific_frame(self):
        """Configura para aplicar a frame específico"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== APLICAR A FRAME ESPECÍFICO ===\n\n", 0.02)
        
        ter.typewrite("Número do frame (0-index): ", 0.02)
        frame_num = int(input())
        
        self.batch_mode = False
        self.config['specific_frame'] = frame_num
        ter.typewrite(ter.Colors.GREEN + f"✓ Efeitos serão aplicados apenas ao frame {frame_num}\n", 0.02)
    
    def preview_effects(self):
        """Visualiza os efeitos em um frame de exemplo"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== PREVIEW DE EFEITOS ===\n\n", 0.02)
        
        if not self.effects_stack:
            ter.typewrite(ter.Colors.YELLOW + "Nenhum efeito configurado ainda.\n", 0.02)
            return
        
        # Carregar frame de exemplo
        input_folder = "../PngFrames"
        png_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".png")])
        
        if not png_files:
            ter.typewrite(ter.Colors.RED + "Nenhum PNG encontrado!\n", 0.02)
            return
        
        sample_frame = png_files[0]
        image_path = os.path.join(input_folder, sample_frame)
        
        with Image.open(image_path) as img:
            ter.typewrite(f"Aplicando {len(self.effects_stack)} efeitos ao frame '{sample_frame}'...\n", 0.02)
            
            # Aplicar todos os efeitos
            processed_img = img.copy()
            for i, effect in enumerate(self.effects_stack):
                ter.print_progress_bar(i + 1, len(self.effects_stack))
                processed_img = self.apply_effect(processed_img, effect)
            
            # Mostrar informações
            ter.typewrite(f"\n\n{ter.Colors.GREEN}✓ Preview concluído!\n", 0.02)
            ter.typewrite(f"Original: {img.size[0]}x{img.size[1]}\n", 0.02)
            ter.typewrite(f"Processado: {processed_img.size[0]}x{processed_img.size[1]}\n", 0.02)
            
            # Salvar preview
            preview_path = "preview_effect.png"
            processed_img.save(preview_path)
            ter.typewrite(f"Preview salvo em: {preview_path}\n", 0.02)
    
    def save_configuration(self):
        """Salva a configuração atual"""
        config = {
            'effects': self.effects_stack,
            'batch_mode': self.batch_mode,
            'config': self.config
        }
        
        config_folder = "../PNGPersonalizer"
        if not os.path.exists(config_folder):
            os.makedirs(config_folder, exist_ok=True)
        
        config_path = os.path.join(config_folder, "customization.json")
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        
        ter.typewrite(ter.Colors.GREEN + f"✓ Configuração salva em {config_path}\n", 0.02)
    
    def load_configuration(self):
        """Carrega uma configuração salva"""
        config_folder = "../PNGPersonalizer"
        config_path = os.path.join(config_folder, "customization.json")
        
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                self.effects_stack = loaded.get('effects', [])
                self.batch_mode = loaded.get('batch_mode', True)
                self.config = loaded.get('config', {})
            
            ter.typewrite(ter.Colors.GREEN + f"✓ Configuração carregada: {len(self.effects_stack)} efeitos\n", 0.02)
        else:
            ter.typewrite(ter.Colors.RED + "Configuração não encontrada!\n", 0.02)
    
    def process_all(self):
        """Processa todos os frames com os efeitos configurados"""
        ter.Clear_all()
        ter.typewrite(ter.Colors.CYAN + "=== PROCESSANDO FRAMES ===\n\n", 0.02)
        
        if not self.effects_stack:
            ter.typewrite(ter.Colors.YELLOW + "Nenhum efeito configurado. Saindo...\n", 0.02)
            return
        
        # Definir pastas
        input_folder = "../PngFrames"
        output_folder = "../PngFrames_Processed"
        
        # Criar backup ou pasta processada
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
        os.makedirs(output_folder, exist_ok=True)
        
        # Listar frames
        png_files = sorted(
            (f for f in os.listdir(input_folder) if f.endswith(".png")),
            key=lambda x: int(os.path.splitext(x)[0])
        )
        
        total_frames = len(png_files)
        if total_frames == 0:
            ter.typewrite(ter.Colors.RED + "Nenhum PNG encontrado!\n", 0.02)
            return
        
        ter.typewrite(f"Processando {total_frames} frames...\n\n", 0.02)
        
        frames_to_process = []
        if self.batch_mode:
            frames_to_process = png_files
        else:
            # Apenas frame específico
            specific = self.config.get('specific_frame', 0)
            if specific < len(png_files):
                frames_to_process = [png_files[specific]]
            else:
                ter.typewrite(ter.Colors.RED + f"Frame {specific} não encontrado!\n", 0.02)
                return
        
        for i, filename in enumerate(frames_to_process):
            input_path = os.path.join(input_folder, filename)
            
            with Image.open(input_path) as img:
                processed_img = img.copy()
                
                # Aplicar todos os efeitos
                for effect in self.effects_stack:
                    processed_img = self.apply_effect(processed_img, effect)
                
                # Salvar
                output_path = os.path.join(output_folder, filename)
                processed_img.save(output_path)
            
            # Progresso
            progress = ((i + 1) / len(frames_to_process)) * 100
            ter.print_progress_bar(i + 1, len(frames_to_process))
        
        ter.typewrite(f"\n\n{ter.Colors.GREEN}✓ Processamento concluído!\n", 0.02)
        ter.typewrite(f"Frames processados: {len(frames_to_process)}\n", 0.02)
        ter.typewrite(f"Salvos em: {output_folder}\n", 0.02)
        
        # Perguntar se quer sobrescrever original
        ter.typewrite("\nDeseja substituir os originais? (1-Sim/2-Não): ", 0.02)
        replace = ter.read_int(1, 2)
        
        if replace == 1:
            # Limpar original e mover processados
            shutil.rmtree(input_folder)
            shutil.move(output_folder, input_folder)
            ter.typewrite(ter.Colors.GREEN + "✓ Originais substituídos!\n", 0.02)

def main():
    """Função principal"""
    ter.Clear_all()
    
    # Banner
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║      PERSONALIZADOR DE FRAMES PNG - GIF2ASC         ║
    ║   Camada intermediária para tratamento de frames    ║
    ╚══════════════════════════════════════════════════════╝
    """
    
    ter.print_centralizedText(ter.Colors.PURPLE + banner)
    
    # Inicializar
    customizer = PNGCustomizer()
    
    # Verificar se há PNGs
    input_folder = "../PngFrames"
    if not os.path.exists(input_folder) or len(os.listdir(input_folder)) == 0:
        ter.typewrite(ter.Colors.RED + "ERRO: Pasta '../PngFrames' vazia ou não existe!\n", 0.02)
        ter.typewrite("Execute primeiro o FrameExtractor.py\n", 0.02)
        sys.exit(1)
    
    # Mostrar menu
    customizer.show_menu()

