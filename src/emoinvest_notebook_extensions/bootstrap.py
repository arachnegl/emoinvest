def load_ipython_extension(ipython):
    from stock_data_importer import stock_import
    ipython.push({
        'stock_import': stock_import,
    })
