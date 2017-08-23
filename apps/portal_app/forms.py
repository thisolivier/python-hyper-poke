def reg_form():
    return """<div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" name="name">
            </div>
            <div class="form-group">
                <label for="fake_name">Pseudonym</label>
                <input type="text" class="form-control" name="fake_name">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" name="email" aria-describedby="emailHelp">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" name="password">
            </div>
            <div class="form-group">
                <label for="password_check">Confirm Password</label>
                <input type="password" class="form-control" name="password_check">
            </div>
            <fieldset class="form-group">
                <legend>Date of Inception</legend>
                <div class="row">
                    <div class="col">
                        <label>Day 
                            <input type="number" name="bday_day" placeholder="DD" class="form-control">
                        </label>
                        <label>Month 
                            <input type="number" name="bday_month" placeholder="MM" class="form-control">
                        </label>
                        <label>Year
                            <input type="number" name="bday_year" placeholder="YYYY" class="form-control">
                        </label>
                    </div>
                </div>
            </fieldset>"""