
class Wbgt():

    def __init__(self, wbgt_value, css_bg_class, description):
        self.wbgt_value = wbgt_value
        self.css_bg_class = css_bg_class
        self.description = description
    
    @classmethod
    def of(cls, templature, humidity):
        
        wbgt_value = Wbgt.__calculate_wbgt(templature, humidity)
        
        if wbgt_value >= 31:
            return Wbgt(wbgt_value, css_bg_class='bg-wbgt-fatal', description='Fatal - 運動は原則中止')
        elif wbgt_value >= 28:
            return Wbgt(wbgt_value, css_bg_class='bg-wbgt-danger', description='Danger - 厳重警戒')
        elif wbgt_value >= 25:
            return Wbgt(wbgt_value, css_bg_class='bg-wbgt-warn', description='Warn - 警戒')
        elif wbgt_value >= 21:
            return Wbgt(wbgt_value, css_bg_class='bg-wbgt-caution', description='Caution - 注意')
        else:
            return Wbgt(wbgt_value, css_bg_class='bg-wbgt-safety', description='Safety - ほぼ安全')
            
    
    # WBGT = 0.735*Ta + 0.0374*RH + 0.00292*Ta*RH – 4.064
    # Ta=室温（℃）、RH=相対湿度（%）
    @staticmethod
    def __calculate_wbgt(templature, humidity):
        return 0.735 * templature + 0.0374 * humidity + 0.00292 * templature * humidity - 4.064

    
    def __str__(self):
        return f"{self.wbgt_value}, description={self.description}, css_bg={self.css_bg_class}"
        
