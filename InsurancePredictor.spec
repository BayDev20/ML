# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['desktop_app.py'],
             pathex=['/Users/cb/Desktop/AI/insurance_predict'],
             binaries=[],
             datas=[('app/templates', 'app/templates'),
                    ('app/static', 'app/static'),
                    ('data', 'data'),
                    ('insurance_predictor.joblib', '.')],
             hiddenimports=['app', 'config'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='InsurancePredictor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='/Users/cb/Desktop/AI/insurance_predict/app/imgs/data.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='InsurancePredictor')
app = BUNDLE(coll,
             name='InsurancePredictor.app',
             icon='/Users/cb/Desktop/AI/insurance_predict/app/imgs/data.ico',
             bundle_identifier=None)
